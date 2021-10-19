import cv2 as cv
import numpy as np
import time
import csv


class ImageRecognition:

    @staticmethod
    def convert_to_hsv(img):
        hsvScale = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        return hsvScale

    @staticmethod
    def convert_to_gray(img):
        grayScale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return grayScale

    @staticmethod
    def centroid_detected(maskin) -> list:

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
    def found_red_particles(img, hsv_scale) -> list:

        lowRed1 = np.array([0, 100, 20], np.uint8)
        highRed1 = np.array([8, 255, 255], np.uint8)
        lowRed2 = np.array([175, 100, 20], np.uint8)
        highRed2 = np.array([179, 255, 255], np.uint8)

        redMask1 = cv.inRange(hsv_scale, lowRed1, highRed1)
        redMask2 = cv.inRange(hsv_scale, lowRed2, highRed2)
        redMask = cv.add(redMask1, redMask2)

        return ImageRecognition.centroid_detected(redMask)

    @staticmethod
    def found_blue_particles(img, hsv_scale) -> list:

        lowBlue = np.array([100, 100, 25], np.uint8)
        highBlue = np.array([125, 255, 255], np.uint8)

        blueMask = cv.inRange(hsv_scale, lowBlue, highBlue)

        return ImageRecognition.centroid_detected(blueMask)

    @staticmethod
    def found_air_particles(img, gray_scale):
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

                airParticles.append({'centroid': (cX, cY), 'radius': r})
                cv.circle(img, (cX, cY), r, (0, 255, 0), 2)
                cv.circle(img, (cX, cY), 1, (0, 255, 0), 3)
        return airParticles

    @staticmethod
    def found_all_particles(img, name) -> dict:
        start = time.time()
        gray_scale = ImageRecognition.convert_to_gray(img)
        hsv_scale = ImageRecognition.convert_to_hsv(img)
        blue_particles = ImageRecognition.found_blue_particles(img, hsv_scale)
        red_particles = ImageRecognition.found_red_particles(img, hsv_scale)
        air_particles = ImageRecognition.found_air_particles(img, gray_scale)
        response = {
            'blue_particles': {
                'particles': blue_particles, 'length': len(blue_particles)
            },
            'red_particles': {
                'particles': red_particles, 'length': len(red_particles)
            },
            'air_particles': {
                'particles': air_particles, 'length': len(air_particles)
            }

        }
        end = time.time()
        print(end-start)

        file = open('status.csv', 'a')
        writer = csv.writer(file)
        writer.writerow([name, end-start, len(air_particles), len(blue_particles),
                        len(red_particles)])
        file.close()
        return response


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(
        'assets/images') if isfile(join('assets/images', f))]
    print(onlyfiles)
    file = open('status.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(['imageName', 'time', 'pa_f', 'pb_f',
                    'pr_f', 'pa_r', 'pb_r', 'pr_r'])
    file.close()
    for name in onlyfiles:
        print(name)
        image = cv.imread(f'assets/images/{name}')
        ImageRecognition.found_all_particles(image, name)
        # cv.imwrite(f'assets/newImages/{name}', image)
