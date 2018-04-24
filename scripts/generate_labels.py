# -*- coding: utf-8 -*-

import geopandas as gpd
import sys
sys.path.append('/home/ubuntu/')
import os
import cv2
from tqdm import tqdm
from magic import  magic
import re
'''
example
/data/imgs/img_001.jpg,837,346,981,456,cow
/data/imgs/img_002.jpg,215,312,279,391,cat
/data/imgs/img_002.jpg,22,5,89,84,bird
/data/imgs/img_003.jpg,,,,,
'''


# def filterCoords(coordinates, image_shape):
# 	xmin, ymin, xmax, ymax = coordinates
# 	image_rows, image_cols, _ = image_shape
# 	xmin_ = max(xmin, 0)
# 	ymin_ = max(ymin, 0)
# 	xmax_ = min(xmax, image_cols)
# 	ymax_ = min(ymax, image_rows)
# 	return [ xmin_, ymin_, xmax_, ymax_]


def filterCoords(coordinates_str, image_data_shape):
	bounds_imcoords_int = [ int(i) for i in coordinates_str.split(',') ]
	bounds_imcoords_int = clipCoords(bounds_imcoords_int, image_data_shape)

	xmin, ymin, xmax, ymax = bounds_imcoords_int	
	status = True

	if (xmin >= xmax) or (ymin>=ymax):
		status = False

	bounds_imcoords_str = ','.join( [str(i) for i in bounds_imcoords_int] )
	return status, bounds_imcoords_str


def clipCoords(coordinates, image_shape):
	rows, cols =  image_shape
	xmin, ymin, xmax, ymax = coordinates
	xmin_ = max(xmin, 0)
	ymin_ = max(ymin, 0)
	xmax_ = min(xmax,  cols-1)
	ymax_ = min(ymax,  rows-1)
	return [ xmin_, ymin_, xmax_, ymax_]


def getClassName2Id(class_id_mapping_path):
	
	dict_classID2Name = {}
	with open(class_id_mapping_path) as f:
		lines = [ line.strip() for line in f.readlines() ]
		for line in lines:
			classId, className = line.split(':')
			dict_classID2Name[classId] = className
	
	dict_classID2Name['75'] = 'unknown1'
	dict_classID2Name['82'] = 'unknown2'
	return dict_classID2Name


def generateRetinaClasses(classDict, outputPath):
	with open(outputPath, 'w') as f:
		for classId, className  in  classDict.items():
			line = str(className) + ',' + classId + '\n'
			f.write(line)
	

def generateRetinaAnnotations(train_json_path, image_dir_path, output_annotations_path):

	dict_imageName_2_shape = getImageNameShapeDict(train_json_path=train_json_path, image_dir_path= image_dir_path)
	data = gpd.read_file(train_json_path)
	with open(output_annotations_path, 'w') as f:
		for idx, row in tqdm(data.iterrows(), total=data.shape[0]):
			try:
				image_name = str(row['image_id'])

				if ('1395.tif' not in image_name):
					image_path = os.path.join(image_dir_path, image_name)
					image_data_shape = dict_imageName_2_shape[image_name]  #cv2.imread(image_path).shape
					bounds_imcoords_str = row['bounds_imcoords'] 
					status, bounds_imcoords_str = filterCoords(bounds_imcoords_str, image_data_shape)

					if status :
						type_id_str = str(row['type_id'])
						class_name = dict_classID2Name[type_id_str]
						line_str = ','.join( [image_path, bounds_imcoords_str, class_name]) 
						line_str += '\n'
						f.write(line_str)
					else:
						print (bounds_imcoords_str, image_name)
			except:
				print (row, '\n\n\n\n')
				raise ValueError('exception----------------------')


def getImageShape(image_path):


	metaStr = magic.from_file(image_path)
	res = re.search(string=metaStr, pattern='height=(\d+).*width=(\d+)')
	if res:
		height, width = res.groups()
	return [int(height), int(width)]


def list_fullpath(dirName, suffix=None):
	if suffix is None:
	 	pathList =  [ os.path.join(dirName, filename) for filename in os.listdir(dirName) ]
	 	        
	else:
	 	pathList =  [ os.path.join(dirName, filename) for filename in os.listdir(dirName)  if filename.endswith(suffix) ]

	pathList = [path for path in pathList if os.path.basename(path)[0].isdigit() ]
	pathList = [path for path in pathList if os.path.isfile(path)]	 	
	return pathList

def getImageShape(image_path):
	metaStr = magic.from_file(image_path)
	res = re.search(string=metaStr, pattern='height=(\d+).*width=(\d+)')
	if res:
		height, width = res.groups()
	return [int(height), int(width)]
 

def getImageNameShapeDict(train_json_path, image_dir_path):
	
	print('------reading images and get image shape-----')
	imagePathList = list_fullpath(image_dir_path)
	dict_imagePath_Name = {}
	for image_path in tqdm(imagePathList, total=len(imagePathList)):
		image_name = os.path.basename(image_path)
		h, w = getImageShape(image_path)  #cv2.imread(image_path).shape			
		dict_imagePath_Name[image_name] = (h, w)
	return dict_imagePath_Name



if __name__ == '__main__':

	xview_train_label_geojson_path = r'../train_labels/xView_train.geojson'
	xview_class_mapping_path = r'../baseline/xview_class_labels.txt'
	xview_train_image_dir_path = r'/home/ubuntu/xview/train_images'

	retina_class_path = r'./classes'
	retina_annotation_path = r'./annotations'

	dict_classID2Name = getClassName2Id(class_id_mapping_path = xview_class_mapping_path)

	print ('start generating classes file')
	generateRetinaClasses(classDict = dict_classID2Name, outputPath = retina_class_path)

	print ('start generating annotation file')
	generateRetinaAnnotations(train_json_path = xview_train_label_geojson_path, \
							  image_dir_path = xview_train_image_dir_path, \
							  output_annotations_path = retina_annotation_path )




 
