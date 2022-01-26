from typing import ClassVar
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt
import cv2

im = io.imread("D:/abc.jpg")
print(im.shape)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(gray.shape)
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img",gray)
cv2.waitKey()