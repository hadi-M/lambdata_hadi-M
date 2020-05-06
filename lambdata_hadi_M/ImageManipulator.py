from PIL import Image
import numpy as np
from pdb import set_trace as st


class ImageManipulator():
    def __init__(self, image_path):
        img_obj = Image.open(image_path)
        self.img_data = np.array(img_obj.getdata()).reshape(img_obj.size[1], img_obj.size[0], 3)
        self.img_size = img_obj.size
        # st()

    def add_to_rgb(self, x):
        # st()
        self.img_data = (self.img_data + 10 ) % 255

    def save(self, file_name):
        X = self.img_data.reshape(self.img_size[0], self.img_size[1], 3)
        X = X.astype("uint8")
        # st()
        img_obj = Image.fromarray(X)
        img_obj.save(file_name)


if __name__ == "__main__":
    image_path = "./test_images/Google_logo.jpg"
    img_man = ImageManipulator(image_path)
    img_man.add_to_rgb(20)
    img_man.save("ff.jpg")