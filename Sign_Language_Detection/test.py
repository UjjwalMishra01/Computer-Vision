import time
from tensorflow import keras
from cvzone.ClassificationModule import Classifier
from cvzone.HandTrackingModule import HandDetector
import cv2 as cv
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np

offset = 20
imgSize = 350
folder = "data/C"
counter = 0
capture = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)
labels = ["A", "B", "C"]
classifier = Classifier("Model/keras_model.h5,Model/labels.txt")

while True:
    success, img = capture.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255  # to get white image we
        # have multiplied it by 255
        imgCropShape = imgCrop.shape

        aspectRatio = h / w
        if aspectRatio > 1:
            const = imgSize / h
            calWidth = math.ceil(const * w)  # so the decimal will always go to higher side
            imgResize = cv.resize(imgCrop, (calWidth, imgSize))
            imgResizeshape = imgResize.shape
            widthGap = math.ceil((350 - calWidth) / 2)
            imgWhite[:, widthGap:calWidth + widthGap] = imgResize
            prediction, index = classifier.getPrediction(img)
            print(prediction,index)
        else:
            const = imgSize / w
            calHeight = math.ceil(const * h)  # so the decimal will always go to higher side
            imgResize = cv.resize(imgCrop, (imgSize, calHeight))
            imgResizeshape = imgResize.shape
            heightGap = math.ceil((350 - calHeight) / 2)
            imgWhite[heightGap:calHeight + heightGap, :] = imgResize

        cv.imshow("Crop Frame", imgCrop)
        cv.imshow("ImgWhite", imgWhite)
    cv.imshow("Image", img)
    key = cv.waitKey(1)


