import cv2 as cv
import numpy as np


class ImageRecognition:

    @staticmethod
    def converTohsv(img):
        hsvScale = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        return hsvScale

    @staticmethod
    def centroidDetected(img, maskin):
        mask = cv.medianBlur(maskin, 7)
        contours = cv.findContours(
            mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
        for i in range(len(contours)):
            cnt = contours[i]
            area = cv.contourArea(cnt)
            if area >= 500:
                M = cv.moments(cnt)
                cX = int(M["m10"]/M["m00"])
                cY = int(M["m01"]/M["m00"])
                cv.circle(img, (cX, cY), 3, (0, 255, 0), -1)

    @staticmethod
    def redParticles(img):
        hsvScale = ImageRecognition.converTohsv(img)

        lowRed1 = np.array([0, 100, 20], np.uint8)
        highRed1 = np.array([8, 255, 255], np.uint8)
        lowRed2 = np.array([175, 100, 20], np.uint8)
        highRed2 = np.array([179, 255, 255], np.uint8)

        redMask1 = cv.inRange(hsvScale, lowRed1, highRed1)
        redMask2 = cv.inRange(hsvScale, lowRed2, highRed2)
        redMask = cv.add(redMask1, redMask2)

        ImageRecognition.centroidDetected(img, redMask)

        return redMask

    @staticmethod
    def blueParticles(img):
        hsvScale = ImageRecognition.converTohsv(img)

        lowBlue = np.array([100, 100, 25], np.uint8)
        highBlue = np.array([125, 255, 255], np.uint8)

        blueMask = cv.inRange(hsvScale, lowBlue, highBlue)

        ImageRecognition.centroidDetected(img, blueMask)

        return blueMask


imagen = cv.imread(
    '/home/eliacer/Descargas/Phantom-Cyto-Seq/Seq/Img000038.jpg')


ImageRecognition.blueParticles(imagen)
ImageRecognition.redParticles(imagen)
cv.imshow("imagen", imagen)
cv.waitKey(0)
cv.destroyAllWindows()
