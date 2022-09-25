import cv2 as cv
import numpy as np
import os



class PreparedImages:
    def __init__(self, imgs_path, first_trashold, second_trashold, prepeared_images_path):
        self.namedir = "\\".join(os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1])
        self.imgs = imgs_path
        self.first_trashold = first_trashold
        self.second_trashold = second_trashold
        self.prepeared_images_path = prepeared_images_path

    # generator that return one read image
    def read_images(self) -> np.array:
        for file_name in os.listdir(self.imgs):
            if "Pr_photos" not in self.imgs + f"\\{file_name}":
                yield cv.imread(self.imgs + f"\\{file_name}")

    # writing image to the path
    def save_image(self, image, path):
        cv.imwrite(str(path), image)


    def convert_image_to_gray(self, image):
        gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        return gray_img





