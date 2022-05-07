import cv2
import time
import mediapipe as mp
camera = cv2.VideoCapture(0)

mpHands =mp.solutions.hands
hands = mpHands.Hands()






while True:
    
    success, img = camera.read()
    imageRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)   

    if results.multi_hand_landmarks:
        for hands in results:
         cv2.imshow("Dont look",img)
         cv2.waitKey(1)
