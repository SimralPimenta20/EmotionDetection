from reldist import get_landmarks
from keras.models import model_from_json

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

c=0
while True:
    r,frame = camera.read()
    cv2.imshow("CHECK!",frame)
    c = c+1
    if c == 100:
        for i in range(n):
            ret,image = camera.read()
            cv2.imshow("CHECK!",image)
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
            print("Anger")
            print((sumanger/m)*100)
            print("Fear:")
            print((sumfear/m)*100)
            print("Happy:")
            print((sumhappy/m)*100)
            print("Neutral:")
            print((sumneutral/m)*100)
            print("Sad:")
            print((sumsad/m)*100)
            c=0
            sumanger = 0
            sumfear = 0
            sumhappy = 0
            sumneutral = 0
            sumsad = 0
            a = []
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
            
            


