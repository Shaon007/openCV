import cv2
import numpy as np

img = cv2.imread("images/OIP.jpeg")
cv2.imshow("bird",img)

blank =np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv2.split(img)
blue= cv2.merge([b,blank,blank])
green= cv2.merge([blank,g,blank])
red= cv2.merge([blank,blank,r])

cv2.imshow('blue',blue)
cv2.imshow("green",green)
cv2.imshow('red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv2.merge([b,g,r])
cv2.imshow('Merged',merged)

cv2.waitKey(0)
