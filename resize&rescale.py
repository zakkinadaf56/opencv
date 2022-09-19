import cv2 as cv

img=cv.imread('photos/download.jpg')       #to red
cv.imshow('download',img)

def rescaleFrame(frame,scale=0.75):      #images,videos,live videos
    width=int(frame.shape[1]*scale)     #1 is indicating width and 0 is indicating height
    height=int(frame.shape[0]*scale)
    dimentions=(width,height)

    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)

reseized_image=rescaleFrame(img)
cv.imshow('Image',reseized_image)

def changetresolution(width,height):   #live videos
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('videos/cat.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=.3)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

