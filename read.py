#Reading images and videos in open cv

import cv2 as cv

#img=cv.imread('photos/download.jpg')       #to red
#cv.imshow('download',img)

#Reading videos
capture=cv.VideoCapture('videos/cat.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)