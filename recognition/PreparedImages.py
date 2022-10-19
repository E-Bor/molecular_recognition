import cv2 as cv
import numpy as np
import os


class PreparedImages:
    """class that needed to prepare images"""
    def __init__(self, imgs_path, first_trashold, second_trashold, prepeared_images_path):
        self.namedir = "\\".join(os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1])
        self.imgs_path = imgs_path
        self.first_thrashold = first_trashold
        self.second_thrashold = second_trashold
        self.prepared_images_path = prepeared_images_path
        self.blurring_kernel_size = (3, 3)

    # generator that return one read image
    def read_images(self) -> np.array:
        for file_name in os.listdir(self.imgs_path):
            if "Pr_photos" not in self.imgs_path + f"\\{file_name}":
                yield cv.imread(self.imgs_path + f"\\{file_name}")

    # writing image to the path
    def save_image(self, image, path) -> None:
        cv.imwrite(str(path), image)

    # convert image to gray and blur
    def convert_image_to_gray_and_blur(self, image, blurring_kernel_size) -> np.array:
        return cv.blur(cv.cvtColor(image, cv.COLOR_BGR2GRAY), blurring_kernel_size)

    def create_all_prepared_images(self) -> None:
        for i in self.read_images():


test = PreparedImages("C:\\Users\\zheny\\PycharmProjects\\molecular_recognition\\Photos", 100, 200,
                      "C:\\Users\\zheny\\PycharmProjects\\molecular_recognition\\Photos\\Pr_photos")
k = 10

for i in test.read_images():
    a = test.convert_image_to_gray_and_blur(i, (3, 3))
    cv.imshow("Source", a)
    #cv.waitKey()
    test.save_image(a, test.prepeared_images_path +f"\\{k}.png")
    k +=1



