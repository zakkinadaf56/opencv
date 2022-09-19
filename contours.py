import cv2 as cv
import numpy as np

img=cv.imread('photos/Bear.jpg')       
cv.imshow('Bear',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blanky',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#canny=cv.Canny(img,125,175)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Canny',thresh)

countours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(countours)}countours found')

new=cv.drawContours(blank,countours,-1,(0,0,255),1)
cv.imshow('CountoursBlank',new)


cv.waitKey(0)