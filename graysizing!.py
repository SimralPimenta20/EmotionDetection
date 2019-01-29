import os
import cv2
import pandas as pd 

path1 ="pics"
path2 = "gray pics"
names_of_images = os.listdir(path1)

c=0
for file in names_of_images:
    im = cv2.imread(path1+'//'+file,1)
    try:
        img = cv2.resize(im,(400,400))
    except:
        print(file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path2 +'//'+file,gray)
