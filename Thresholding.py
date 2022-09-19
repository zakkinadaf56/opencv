import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('photos/Tiger.jpg')
cv.imshow('Bdear',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#simple thresholding-->Manualy set the threshold value 
threshold,thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('SimpleThresh',thresh)
threshold,thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('SimpleThresh_inv',thresh_inv)

#Adaptive thresholding-->Open cv set the threshold value dynamically for us
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('ADaptive_thresholding',adaptive_thresh)

cv.waitKey(0)