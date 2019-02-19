import numpy as np
import cv2

cap = cv2.VideoCapture(0)#mention your camera port
 
while(True):#loop
    ret, frame = cap.read() #read frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    #cv2.imshow('frame',gray)#color gray or simple color
    #
    cv2.imshow('frame',frame) #colorfull frame used
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()#release 
cv2.destroyAllWindows()
