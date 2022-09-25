import cv2 as cv
import numpy as np



class ImageContour:
    def __init__(self, prepared_image_path):
        self.prepared_images_path = prepared_image_path

    def get_edge(self, first_threshold, second_threshold):
        ...

    def find_contour(self, image, contour):
        ...