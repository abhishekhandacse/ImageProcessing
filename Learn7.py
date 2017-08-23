import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#   Hsv is hue saturation value
    lower_red=np.array([150,25,20])
    upper_red=np.array([200,150,150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel=np.ones((15,15),np.float32)/255
    smoothed=cv2.filter2D(res,-1,kernel)
    median=cv2.medianBlur(res,15)
    blur=cv2.GaussianBlur(res,(15,15),0)
    bilateral=cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('Blurry', smoothed)
    cv2.imshow('Gausian', blur)
    cv2.imshow('Median', median)
    cv2.imshow('Bilateral', bilateral)

    k=cv2.waitKey(5) & 0xFF
    if k==2:
        break

cv2.destroyAllWindows()
cap.release()