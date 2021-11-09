#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 04:19:37 2021

@author: basuki
"""
import cv2

# get camera
cam =  cv2.VideoCapture(0)
cam.set(3, 640) #lebar
cam.set(4, 480) #tinggi
facedetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#cath frame by frame
while True:
   retV, frame = cam.read()

   abu2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   faces = facedetector.detectMultiScale(abu2, 1.3, 5) #frame, scale factor, 

   for(x, y, w, h) in faces:
       
       frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)
       
   cv2.imshow('tes', frame)
   # cv2.imshow('tes-abu abu', abu2)
   
   k = cv2.waitKey(1) & 0xFF
   
   if k == 27 or k == ord('q'):
       break
   
cam.release()
cv2.destroyAllWindows()
       