import cv2
import numpy as np
img= cv2.imread("images/OIP.jpeg")
cv2.imshow("image",img)

blank= np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('blank image',blank)

mask= cv2.circle(blank, (img.shape[1]//2-80,img.shape[0]//2-100),100,255,-1)
#                             +- values to move the circle to get bird head
cv2.imshow('mask',mask)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('masked',masked)

cv2.waitKey(0)

