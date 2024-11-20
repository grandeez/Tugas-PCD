# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:07:42 2024

@author: ASUS
"""

#konversi warna ke Abu-abu 
import cv2 
import numpy as np


img = cv2.imread("C:\\Users\\ASUS\\Downloads\\foto salju.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(tresh, BW) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

print("Original = ", img.shape)
print("Gray = ", gray.shape)
print("BW = ", BW.shape)
print(BW)
cv2.imwrite("Hasil.png", BW)

cv2.waitKey(0)
cv2.destroyAllWindows()