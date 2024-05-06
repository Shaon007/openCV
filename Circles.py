import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('blank',blank)

cv2.circle(blank,(250,250),(50),(200,0,0),thickness=2)
              #    center   radius  color
cv2.imshow('Circles',blank)
cv2.waitKey(0)
cv2.line(blank,(100,250),(300,100),(200,0,0),thickness=2)
cv2.imshow('lines', blank)

cv2.waitKey(0)
