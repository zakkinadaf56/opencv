import cv2 as cv
from cv2 import rectangle
import numpy as np
import matplotlib.pyplot as pl

blank=np.zeros((400,400),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#Bitwise And-->intersecting region
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('And',bitwise_and)

#Bitwise Or-->intyersecting and non-intersecting region

bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Or',bitwise_or)

#bitwise xor-->non-intersecting region
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Xor',bitwise_xor)

#bitwise not
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('Not',bitwise_not)

cv.waitKey(0)