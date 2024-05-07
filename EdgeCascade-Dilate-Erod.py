import cv2
import numpy as np

img =cv2.imread('images/OIP.jpeg')

cv2.imshow('birds',img)

canny = cv2.Canny(img,125,175)
cv2.imshow('Canny',canny)

#Dilating the image
dilated = cv2.dilate(canny,(7,7),iterations=1)
cv2.imshow("Dialeted",dilated)

#Eroded Image
eroded = cv2.erode(dilated,(7,7),iterations=1)
cv2.imshow("eroded",eroded)

cv2.waitKey(0) 
