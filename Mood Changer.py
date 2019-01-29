from reldist import get_landmarks
from keras.models import model_from_json
from app import happy,anger,neutral,sad,fear

import json
import cv2
import dlib
import numpy as np

camera = cv2.VideoCapture(0)
a=[]
n = 10
sumanger = 0
sumfear = 0
sumhappy = 0
sumneutral = 0
sumsad = 0
json_file = open('s.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("s.h5")

emotion = []
c=0
while True:
    r,frame = camera.read()
    cv2.imshow("MOOD UP!",frame)
    c = c+1
    if c == 100:
        for i in range(n):
            ret,image = camera.read()
            cv2.imshow("MOOD UP!",image)
            img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            a.append(get_landmarks(img))
            
        b = np.array(a)   
        try:
            prediction = loaded_model.predict(b)
            for i in range(n):
                sumanger = sumanger+prediction[i][0]
                sumfear = sumfear+prediction[i][1]
                sumhappy = sumhappy+prediction[i][2]
                sumneutral = sumneutral+prediction[i][3]
                sumsad = sumsad+prediction[i][4]
            m = float(n)
            emotion.append(sumanger/m)
            emotion.append(sumfear/m)
            emotion.append(sumhappy/m)
            emotion.append(sumneutral/m)
            emotion.append(sumsad/m)
            break
        except:
            print ("Your face didn't get detected!")
            c=0
            a = []
            pass
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
                
camera.release()
cv2.destroyAllWindows()

max1 = 0
for i in range(5):
    if emotion[i] > max1:
        max1 = emotion[i]
        b = i
if emotion[4] > 0.11:
    b = 4
if (emotion[3] > 0.10) and (emotion[4] > 0.11):
    b = 3
if (emotion[4] > 0.11) and (emotion[1]>0.27):
    b = 1
if (emotion[4] > 0.11) and (emotion[0]>0.34):
    b = 0
if b == 0:
    anger()
if b == 1:
    fear()
if b == 2:
    happy()
if b == 3:
    neutral()
if b == 4:
    sad()
            
            


