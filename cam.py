import cv2
import requests
import numpy as np
import imutils
import tensorflow as tf
from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import glob
from matplotlib import pyplot
import pandas as pd
import os

url = "http://192.168.50.102:8080/shot.jpg"

# While loop to continuously fetching data from the Url
while True:
    
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    #img = imutils.resize(img, width=1080, height=1920)
        
    cv2.imshow('img',img)

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
      cv2.imwrite('sample.jpg',img)
      break
  
cv2.destroyAllWindows()