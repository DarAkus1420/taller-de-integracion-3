import cv2 as cv
import stapi as st
import numpy as np
import requests


class ImageRecognition:

    """
    Class used to analyze different images, and to be able
    to found red, blue and gray particles
    """
    @staticmethod
    def convert_to_hsv(img):
        """Convert the image to a hsv scale

        Parameters
        ----------
        img: array
            The image to be converted to hsv scale

        Returns
        -------
        hsvScale
            The hsv scale obtained from the image
        """
        hsvScale = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        return hsvScale

    @staticmethod
    def convert_to_gray(img):
        """Convert the image to a gray scale

        Parameters
        ----------
        img: array
            The image to be converted to gray scale

        Returns
        -------
        grayScale 
            The gray scale obtained from the image
        """
        grayScale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return grayScale

    @staticmethod
    def centroid_detected(maskin) -> list:
        """Get the centroid from a image, and get the particles

        Parameters
        ----------
        maskin: array
            TODO

        Returns
        -------
        particles 
            The particles founded in the image
        """
        particles = []
        mask = cv.medianBlur(maskin, 7)
        contours = cv.findContours(
            mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]

        for cnt in contours:
            area = cv.contourArea(cnt)
            perimeter = cv.arcLength(cnt, True)
            if area >= 500:
                M = cv.moments(cnt)
                cX = int(M["m10"]/M["m00"])
                cY = int(M["m01"]/M["m00"])
                radius = perimeter/(2*np.pi)
                particles.append([cX, cY, radius])
        return particles

    @staticmethod
    def found_red_particles(hsv_scale) -> list:

        lowRed1 = np.array([0, 100, 20], np.uint8)
        highRed1 = np.array([8, 255, 255], np.uint8)
        lowRed2 = np.array([175, 100, 20], np.uint8)
        highRed2 = np.array([179, 255, 255], np.uint8)

        redMask1 = cv.inRange(hsv_scale, lowRed1, highRed1)
        redMask2 = cv.inRange(hsv_scale, lowRed2, highRed2)
        redMask = cv.add(redMask1, redMask2)

        return ImageRecognition.centroid_detected(redMask)

    @staticmethod
    def found_blue_particles(hsv_scale) -> list:

        lowBlue = np.array([100, 100, 25], np.uint8)
        highBlue = np.array([125, 255, 255], np.uint8)

        blueMask = cv.inRange(hsv_scale, lowBlue, highBlue)

        return ImageRecognition.centroid_detected(blueMask)

    @staticmethod
    def found_air_particles(gray_scale):
        airParticles = []

        # Uncomment one of the variables named grayBlur and
        # comment out the other to test the difference in performance.

        # grayBlur = cv.blur(grayScale, (4, 4))
        grayBlur = cv.bilateralFilter(gray_scale, 5, 75, 75)
        detectedCircle = cv.HoughCircles(
            grayBlur, cv.HOUGH_GRADIENT, 1, 2, param1=40, param2=15, minRadius=9, maxRadius=12)

        if detectedCircle is not None:
            detectedCircle = np.uint16(np.around(detectedCircle))

            for dC in detectedCircle[0, :]:
                cX = dC[0]
                cY = dC[1]
                r = dC[2]

                airParticles.append([cX, cY, r])
        return airParticles

    @staticmethod
    def found_all_particles(img, url: str) -> dict:
        gray_scale = ImageRecognition.convert_to_gray(img)
        hsv_scale = ImageRecognition.convert_to_hsv(img)
        blue_particles = ImageRecognition.found_blue_particles(hsv_scale)
        red_particles = ImageRecognition.found_red_particles(hsv_scale)
        air_particles = ImageRecognition.found_air_particles(gray_scale)
        gray_array = np.array(air_particles, dtype=np.float32)
        red_array = np.array(red_particles, dtype=np.float32)
        blue_array = np.array(blue_particles, dtype=np.float32)
        emulator_response = {

            'blue_particles': {
                'particles': blue_array, 'length': len(blue_particles)
            },
            'red_particles': {
                'particles': red_array, 'length': len(red_particles)
            },
            'air_particles': {
                'particles': gray_array, 'length': len(air_particles)
            }

        }
        response = {
            "blue_particles": blue_particles,
            "red_particles": red_particles,
            "air_particles": air_particles

        }
        requests.post(url, json={'data': str(response)})

        return emulator_response
