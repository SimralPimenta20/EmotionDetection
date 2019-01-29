import cv2
import numpy as np
import dlib
import math
detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks (1).dat")


def get_landmarks(image):
    detections = detector(image, 1)
    for k,d in enumerate(detections): #For all detected face instances individually
        shape = predictor(image, d) #Draw Facial Landmarks with the predictor class
        xlist = []
        ylist = []
        for i in range(0,68): #Store X and Y coordinates in two lists
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))
            
        xmean = np.mean(xlist) #Find both coordinates of centre of gravity
        ymean = np.mean(ylist)
        #xcentral = [(x-xmean) for x in xlist] #Calculate distance centre <-> other points in both axes
        #ycentral = [(y-ymean) for y in ylist]
        reldis = []
        for i in range(0,68):
                reldis.append(math.sqrt((xmean-xlist[i])**2+(ymean-ylist[i])**2))
        
        return reldis




























        
        
      
