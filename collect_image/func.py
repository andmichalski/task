import urllib.request

import cv2 as cv
import numpy as np


def get_image(url):
    data = urllib.request.urlopen(url)
    image = np.asarray(bytearray(data.read()), dtype="uint8")
    image = cv.imdecode(image, cv.IMREAD_COLOR)

    return image


def find_right_text_size(image, text):
    buffer_height = 200
    image = cv.copyMakeBorder(image, buffer_height, 0, 0, 0, cv.BORDER_CONSTANT, value=[255, 255, 255])
    _, width_image, _ = image.shape

    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thick = 3
    text_size = cv.getTextSize(text, font, font_scale, font_thick)
    while text_size[0][0] > width_image:
        font_scale -= 0.1
        text_size = cv.getTextSize(text, font, font_scale, font_thick)
        if font_scale == 0 and font_thick == 0:
            print("Image to small to put text")
            return
    image = cv.putText(image, text, (20, 150), font, font_scale, (0, 0, 0), font_thick)
    return image


def show_images(img):
    cv.namedWindow('image', cv.WINDOW_NORMAL)

    grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    grey_3_channel = cv.cvtColor(grey, cv.COLOR_GRAY2BGR)

    _, thresh = cv.threshold(grey_3_channel, 127, 255, cv.THRESH_BINARY)

    compared_images = np.concatenate((img, thresh), axis=1)

    text = "Type key s to save binary as bin_image.jpg in task folder or type other keys to not save"

    compared_images_with_text = find_right_text_size(compared_images, text)

    cv.imshow('image', compared_images_with_text)

    k = cv.waitKey()
    if k == 115:
        cv.imwrite("bin_image.jpg", thresh)
    cv.destroyAllWindows()
