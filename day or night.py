# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:03:50 2024

@author: ASUS
"""

import numpy as np
import cv2
import argparse
import sys, inspect, os

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "..","..", "Image_Lib")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

# import image_utils as utils

def image_resize(image, width=-1, height=-1):
    shape = image.shape
    if width == -1:
        if height == -1:
            return image
        else:
            return cv2.resize(image, (int(height * shape[1] / shape[0]), height))
    elif height == -1:
        return cv2.resize(image, (width, int(width * shape[0] / shape[1])))
    else:
        cv2.resize(image, (width, height))

# ap = argparse.ArgumentParser("Simple intensity measure to detect Day or Night picture")
# ap.add_argument("-i", "--image", required = True, help = "Path to image file")
# ap.add_argument("-f", required=False)
# args = vars(ap.parse_args())

# image = cv2.imread(args["C:/Users/ASUS/Downloads/corgi.jpg"])
image = cv2.imread("C:/Users/ASUS/Downloads/man.jpg")
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h,s,v) = cv2.split(imageHSV)
brightPixelCount = np.sum(v > 128)
pixelCount = image.shape[0]*image.shape[1]

if(brightPixelCount > pixelCount/2):
    print ("DAY")
else:
    print ("NIGHT")

cv2.imshow("Image", image_resize(image, height = 600))
cv2.waitKey()
cv2.destroyAllWindows()
