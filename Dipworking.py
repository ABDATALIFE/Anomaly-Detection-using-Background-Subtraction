import numpy as np
import cv2
import time


cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True) 
kernelOp = np.ones((3,3),np.uint8)
kernelCl = np.ones((11,11),np.uint8)



cap.set(3,640) #set width
cap.set(4,480) #set height

w = cap.get(3) #get width
h = cap.get(4) #get height

mx = int(w/2)
my = int(h/2)




while(True):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
	cv2.line(frame,(mx,0),(mx,h),(0,255,0),3)

    cv2.imshow('frame',frame)
	cv2.imshow('BackgroundSubtraction',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()