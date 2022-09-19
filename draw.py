import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3), dtype='uint8')  #uint8 is a data type of an image
cv.imshow('Blank',blank)
#cv.imshow('Lion',img)
#img=cv.imread('photos/lion.jpg')

#1.Paint The image
#blank[:]=0,0,255
#cv.imshow('Green',blank)

#draw a rectangle
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)  #to fill the rectangle use cv.FILLED or -1
#cv.imshow('Reactangle',blank)

#draw a circle
#cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
#cv.imshow('Circle',blank)

#draw a line
#cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
#cv.imshow('Line',blank)

#write text in an image
cv.putText(blank,'Hello everyone',(130,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)