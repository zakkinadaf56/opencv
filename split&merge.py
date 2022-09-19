import cv2 as cv
import numpy as np
import matplotlib.pyplot as pl

img=cv.imread('photos/lion.jpg')       
cv.imshow('lion',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(img.shape)
print(g.shape)
print(b.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow('Merged',merged)


cv.waitKey(0)