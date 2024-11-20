# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:00:35 2024

@author: ASUS
"""

# rotasi
import cv2
import numpy as np
img = cv2.imread("C:\\Users\\ASUS\\Downloads\\foto salju.jpg",0)
rows, cols = img.shape
MRotasi = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)

print(MRotasi)

dstRotasi = cv2.warpAffine(img, MRotasi, (cols, rows))

cv2.imshow("dstRotasi",dstRotasi)

cv2.waitKey(0)
cv2.destroyAllWindows()