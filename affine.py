# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:01:47 2024

@author: ASUS
"""

# Affine
import cv2
import numpy as np
img = cv2.imread("C:\\Users\\ASUS\\Downloads\\foto salju.jpg",0)
rows, cols = img.shape
ttkAsal = np.float32([[172,109], [282,65], [272,316]])
ttkTujuan = np.float32([[53,128], [471,46], [275, 385]])

MAffine = cv2.getAffineTransform(ttkAsal, ttkTujuan)

print(MAffine)

dstAffine = cv2.warpAffine(img, MAffine, (cols, rows))

cv2.imshow("dstAffine",dstAffine)

cv2.waitKey(0)
cv2.destroyAllWindows()