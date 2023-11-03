import cv2 as cv
import time
import numpy
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
################################
wCam, hCam = 640, 480
################################
capture = cv.VideoCapture(0)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]     #minimum volume is at 0 and maximum volume is at 1
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
while True:
    success, img = capture.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx = (x1 + x2) //2
        cy = (y1 + y2) //2
        cv.circle(img, (x1, y1), 15, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x2, y2), 15, (255, 0, 255), cv.FILLED)
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 5)
        cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)
        # Hand Range 50-300. Now we have to convert it into our volume range  -65-0
        vol = numpy.interp(length, [50, 300], [minVol, maxVol])
        volBar = numpy.interp(length, [50, 300], [400, 150])
        volPer = numpy.interp(length, [50, 300], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length < 50:
            cv.circle(img, (cx, cy), 15, (0, 255, 0), cv.FILLED)
    cv.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)   # used to create a sound bar
    cv.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv.FILLED)
    cv.putText(img, f'{int(volPer)} %', (40, 450), cv.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (40, 50), cv.FONT_HERSHEY_COMPLEX,
               1, (0, 0, 255), 1)
    cv.imshow("Img", img)
    cv.waitKey(1)
