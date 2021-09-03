import cv2
import numpy as np
import HandTrackingProject.HandTrackingModule as htm
import time
import autopy

wCam, hCam = 640, 480
wScr, hScr = autopy.screen.size()
print(wScr,hScr)
frameR = 120 # frame reduction
smoothening = 7

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1,detectionCon=0.8)

pTime= 0
pLocX, pLocY = 0, 0
cLocX, cLocY = 0, 0

while True:
    success, img = cap.read()
    # find hand landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    #get the tip and middle finger
    if len(lmList)!=0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    # check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        # Only index finger: moving mode
        if fingers[1]==1 and fingers[2]==0:

            x3 = np.interp(x1, (frameR, wCam-frameR),(0,wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
            # convert coordinates

            # smoothing values
            cLocX = pLocX + (x3- pLocX) / smoothening
            cLocY = pLocY + (y3 - pLocY) / smoothening

        # move mouse
            autopy.mouse.move(wScr-cLocX,cLocY)
            cv2.circle(img,(x1,y1), 15,(255,0,255), cv2.FILLED)
            pLocX, pLocY = cLocX, cLocY
        # Both index and middle finger : clicking mode
        if fingers[1] == 1 and fingers[2] == 1:

            # find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)
            # click mouse if distance is short
            if length < 25:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    cv2.imshow('Image', img)
    cv2.waitKey(1)