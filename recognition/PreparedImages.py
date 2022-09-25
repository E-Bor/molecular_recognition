import cv2 as cv



class PreparedImages:
    def __init__(self, imgs_path, first_trashold, second_trashold, prepeared_images_path):
        self.imgs = imgs_path
        self.first_trashold = first_trashold
        self.second_trashold = second_trashold
        self.prepeared_images_path = prepeared_images_path

    def read_image(self):
        ...

    def save_image(self):
       ...

    def convert_image_to_gray(self):
        gray_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        return gray_img




