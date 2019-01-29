from numpy import array
from reldist import get_landmarks
from PIL  import Image
import pandas as pd 
import csv
import cv2

path1 = "gray pics"

with open('1.csv','rt') as inp,open('2.csv','wt') as out:
    writer = csv.writer(out)    
    for row in csv.reader(inp):
        m=(array([array(Image.open(path1+'//'+row[1]))]))
        for n in m:
            if get_landmarks(n) != None:
                writer.writerow(row)

      
