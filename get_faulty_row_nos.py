import os
import pandas as pd
from reldist import get_landmarks
from PIL import Image
from numpy import array

data = pd.read_csv("2.csv")
path1 = "gray pics"

c = 0
imlist = data.iloc[0:277,1]


X_train1 = array([array(Image.open(path1+'//'+a))for a in imlist])
for file in X_train1:
    c=c+1
    try:
        b = len(get_landmarks(file))
    except:
        print (c)
        continue
#a = get_landmarks(X_train1[0])
#print(a)
