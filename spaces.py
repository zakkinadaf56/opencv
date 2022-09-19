import cv2 as cv
import numpy as np
import matplotlib.pyplot as pl

img=cv.imread('photos/Bear.jpg')       
cv.imshow('Bear',img)

#pl.imshow(img)
#pl.show()

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV(Hiew Saturation Value)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*a*b

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#HSV TO BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

#LAB TO BGR
LAB_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB_bgr',LAB_bgr)

#RGB TO BGR
RGB_bgr=cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
cv.imshow('RGB_bgr',RGB_bgr)

cv.waitKey(0)

#1:13:07