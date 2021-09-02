import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = 'Header'
myList = os.listdir(folderPath)

overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
header = overlayList[0]
drawColor = (0,0,255)
brushThickness = 15
eraserThickness = 45

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.9)
imgCanvas = np.zeros((480,640,3), np.uint8)

xp, yp = 0,0

while True:
    # Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        # tip of index and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # Check which fingers are up
        fingers = detector.fingersUp()

        # IF selection mode - two fingers up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            if y1 < 125:
                if 70<x1<180:
                    header = overlayList[0]
                    drawColor = (0,0,255)
                elif 180<x1<320:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)
                elif 320<x1<450:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 450<x1<580:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 20), (x2, y2 + 20), drawColor, cv2.FILLED)
        # IF drawing mode - index up
        elif fingers[1] and fingers[2] == False:
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0,0,0):
                cv2.circle(img, (x1, y1), eraserThickness, drawColor, cv2.FILLED)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.circle(img, (x1, y1), brushThickness, drawColor, cv2.FILLED)
                cv2.line(img, (xp,yp), (x1,y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray,50,255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img,imgCanvas)

    # setting the header image
    img[0:90,0:640] = header
    #img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5,0)
    cv2.imshow('Image', img)
    #cv2.imshow('Canvas', imgCanvas)
    cv2.waitKey(1)