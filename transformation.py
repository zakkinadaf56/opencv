import cv2 as cv
import numpy as np

img=cv.imread('photos/download1.jpg')       
cv.imshow('download1',img)

#translation
def translate(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimentions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimentions)

#-x -->left
#-y -->up
#x -->Right
#y -->down

translated=translate(img,100,100)
cv.imshow('Translated',translated)

#Rotation

def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]

    if rotpoint==None:
        rotpoint=(width//2,height//2)
    
    rotmat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimentions=(width,height)
    return cv.warpAffine(img,rotmat,dimentions)

rotated=rotate(img,45)
cv.imshow('Rotated',rotated)

rotated2=rotate(img,90)
cv.imshow('Rotated2',rotated2)

#resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#flipping
flipped=cv.flip(img,1)
cv.imshow('Flipped',flipped)

#cropping
cropped=img[100:150,80:90]
cv.imshow('Crpeed',cropped)

cv.waitKey(0)