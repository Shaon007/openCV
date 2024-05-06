import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('blank',blank)

cv2.rectangle(blank,(0,0),(300,300),(200,0,0), thickness=2)
# rectangle parameter points of start to end, color, thickness

cv2.rectangle(blank,(0,0),(300,300),(200,0,0), thickness=-1)
#if the thickness = cv2.FILLED or thickness = -1  than fils the box with solid color

cv2.imshow('Rectangle', blank)

cv2.waitKey(0)
