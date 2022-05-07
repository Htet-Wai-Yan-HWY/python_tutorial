import cvzone.HandTrackingModule as htm
import cv2
import os
import time


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.HandDetector(detectionCon=0.8)

pTime = 0

while True:
    succes, img = cap.read()
   
    img = detector.findHands(img)
    

  
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Don't LOOK",img)
    cv2.waitKey(1)
