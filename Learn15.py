#Forwarding Extraction or Backword Elemination
import cv2
import numpy as np
cap=cv2.VideoCapture('Street.mp4')
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)

    cv2.imshow('Original',frame)
    cv2.imshow('fg',fgmask)

    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()