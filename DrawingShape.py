import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #creates blank canvas to draw on,,also can use img
cv2.imshow('Blank',blank)

# paint the img a certain color
blank[:] = 0,255,0 #BGR color value 0,x,0 for green band, x00 for blue, 00x for red, multiple for mixing and creating new color
#blank[:] for color parameter, if range given,certain area is colored

blank[200:300, 300:400]= 0,0,255

cv2.imshow('green',blank)

cv2.waitKey(0)
