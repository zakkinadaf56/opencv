import cv2 as cv

img=cv.imread('photos/lion.jpg')
cv.imshow('Lion',img)



#Converting an image to gray scale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#how to blur an image

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)

#dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding
eroded=cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded',eroded)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) #to enlarge INTER.LINEAR/CUBIC ,to reduce INTER.AREA
cv.imshow('Resized',resized)

#cropping
cropped=resized[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)