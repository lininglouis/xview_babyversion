# xview_babyversion

 
0) make sure you have the same folder struct

1) download the geojson files, and baseline folder from xview organization. download the train, val, train_label data.
Below is the folder structure I used.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;./xview

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'./train_images'   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'./val_images'

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'./train_labels/xView_train.geojson'

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'./baseline/xview_class_labels.txt'

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'./scripts/*'



2) cd folder 'script'

3) run the command below. It will parse the label json file, and generate an annotation file and a classes file in csv format. They are saved in the same local direcotry.
```
python generate_labels.py
```

&nbsp;&nbsp;The generated annotation file format looks like : (if a image does not contain any target object, and you wanna train the as the negatives, their bouding box will be empty, as the last line shows.
 ```
/data/imgs/img_001.jpg,837,346,981,456,cow
/data/imgs/img_002.jpg,215,312,279,391,cat
/data/imgs/img_002.jpg,22,5,89,84,bird
/data/imgs/img_003.jpg,,,,,  
```

 
