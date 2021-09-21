import cv2 as cv
import numpy as np


class ImageRecognition:

    @staticmethod
    def conver_to_hsv(img):
        hsvScale = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        return hsvScale

    @staticmethod
    def centroid_detected(img, maskin) -> list:

        particles = []
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
                particles.append({'centroid': (cX, cY)})
        return particles

    @staticmethod
    def found_red_particles(img) -> list:
        hsvScale = ImageRecognition.conver_to_hsv(img)

        lowRed1 = np.array([0, 100, 20], np.uint8)
        highRed1 = np.array([8, 255, 255], np.uint8)
        lowRed2 = np.array([175, 100, 20], np.uint8)
        highRed2 = np.array([179, 255, 255], np.uint8)

        redMask1 = cv.inRange(hsvScale, lowRed1, highRed1)
        redMask2 = cv.inRange(hsvScale, lowRed2, highRed2)
        redMask = cv.add(redMask1, redMask2)

        return ImageRecognition.centroid_detected(img, redMask)

    @staticmethod
    def found_blue_particles(img) -> list:
        hsvScale = ImageRecognition.conver_to_hsv(img)

        lowBlue = np.array([100, 100, 25], np.uint8)
        highBlue = np.array([125, 255, 255], np.uint8)

        blueMask = cv.inRange(hsvScale, lowBlue, highBlue)

        return ImageRecognition.centroid_detected(img, blueMask)

    @staticmethod
    def found_all_particles(img) -> dict:
        blue_particles = ImageRecognition.found_blue_particles(img)
        red_particles = ImageRecognition.found_red_particles(img)
        response = {
            'blue_particles':
                {
                    'particles': blue_particles, 'length': len(blue_particles)
                },
            'red_particles':
                {
                    'particles': red_particles, 'length': len(red_particles)
                }

        }
        return response


if __name__ == '__main__':
    imagen = cv.imread(
        './Img000038.jpg')
    print(ImageRecognition.found_all_particles(imagen))
