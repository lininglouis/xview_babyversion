# xview_babyversion

1) make sure you've download the geojson files, and baseline folder from xview organization
geojson file path looks like './train_labels/xView_train.geojson'
classname and id file path looks like  './baseline/xview_class_labels.txt'


2) cd folder 'script'
3) run the command. Parse the label json file, and generate label in txt  
```
python generate_labels.py
```

The generated annotation file format looks like :
 ```
/data/imgs/img_001.jpg,837,346,981,456,cow
/data/imgs/img_002.jpg,215,312,279,391,cat
/data/imgs/img_002.jpg,22,5,89,84,bird
/data/imgs/img_003.jpg,,,,,
```

 
