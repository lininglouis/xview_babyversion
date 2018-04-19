# xview_babyversion

这个repo是为了能够解压geojson文件，生成csv文本格式的标注信息，用于其他模型训练。
解压后的标注文件扔掉了地理坐标等信息，如果后面需要这个需要再想办法加进去。


1) make sure you've download the geojson files, and baseline folder from xview organization
geojson file path looks like './train_labels/xView_train.geojson'
classname and id file path looks like  './baseline/xview_class_labels.txt'

2) cd folder 'script'
3) run the command. It will parse the label json file, and generate an annotation file and a classes file in csv format
```
python generate_labels.py
```

&nbsp;&nbsp;The generated annotation file format looks like :
 ```
/data/imgs/img_001.jpg,837,346,981,456,cow
/data/imgs/img_002.jpg,215,312,279,391,cat
/data/imgs/img_002.jpg,22,5,89,84,bird
/data/imgs/img_003.jpg,,,,,
```

 
