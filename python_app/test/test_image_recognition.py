
import unittest
from modules.ImageRecognition.ImageRecognition import ImageRecognition
import cv2 as cv


class TestResponses(unittest.TestCase):
    def test_blue_particles(self):

        image = cv.imread('assets/Img000038.jpg')
        blue_particles = ImageRecognition.found_blue_particles(image)
        self.assertEqual(len(blue_particles), 1)

    def test_red_particles(self):

        image = cv.imread('assets/Img000038.jpg')
        red_particles = ImageRecognition.found_red_particles(image)
        self.assertEqual(len(red_particles), 1)
