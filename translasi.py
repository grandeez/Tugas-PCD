# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:00:00 2024

@author: ASUS
"""

# translasi
import cv2
import numpy as np
img = cv2.imread("C:\\Users\\ASUS\\Downloads\\foto salju.jpg",0)
print(img.shape)

rows, cols = img.shape

MTranslasi = np.float32([[2, 0, 100],[0, 2, 50]])

print(MTranslasi, '\n')


dst = cv2.warpAffine(img, MTranslasi, (cols, rows))

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()