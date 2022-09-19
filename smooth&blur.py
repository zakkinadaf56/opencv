import cv2 as cv
import numpy as np
import matplotlib.pyplot as pl

img=cv.imread('photos/tiger.jpg')       
cv.imshow('tiger',img)

#Averaging
average=cv.blur(img,(3,3))
cv.imshow('Average',average)

#Gaussian Blur

gaussian=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian',gaussian)

#Median Blur
median=cv.medianBlur(img,3)
cv.imshow('median',median) 

#bilateral
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)


cv.waitKey(0)