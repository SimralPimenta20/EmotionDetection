from reldist import get_landmarks
from keras.preprocessing.image import load_img,array_to_img
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.layers import Conv2D,MaxPooling2D
from keras.models import model_from_json
import json


import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from numpy import array
import sys
import pandas as pd
from sklearn import preprocessing
sys.__stdout__ = sys.stdout

data = pd.read_csv("2.csv")
path1 = "gray pics"
training_data = data.iloc[0:222,1]
training_ans = data.iloc[0:222,2]
test_data = data.iloc[223:277,1]
test_ans = data.iloc[223:277,2]
imlist = training_data
imlist1 = test_data
le = preprocessing.LabelEncoder()
le.fit(training_ans)
le1 = preprocessing.LabelEncoder()
le1.fit(test_ans)

X_train1 = array([array(Image.open(path1+'//'+a))
                  for a in imlist])

X_train2 = []

for file in X_train1:
    X_train2.append(get_landmarks(file))
    

y_train =le.transform(training_ans)

X_test1 = array([array(Image.open(path1  + '//' + b))
                 for b in imlist1])

X_test2 = []

for file in X_test1:
    X_test2.append(get_landmarks(file))
    
y_test = le1.transform(test_ans)
X_train = np.array(X_train2)
X_test = np.array(X_test2)
y_test = to_categorical(y_test,5)
y_train = to_categorical(y_train,5)

model = Sequential()
model.add(Dense(1080,activation = 'sigmoid',input_shape=(68,)))
model.add(Dense(1080,activation = 'sigmoid'))
model.add (Dense(5,activation = 'softmax'))
model.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics=['accuracy'])
model.summary()
history = model.fit(X_train,y_train,epochs=20,validation_data = (X_test,y_test))
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.plot(history.history['loss'])

s_json =model.to_json()
with open("s.json","w") as json_file:
	json_file.write(s_json)
model.save_weights("s.h5")



