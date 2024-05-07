import cv2
import numpy as np

img = cv2.imread('images/OIP.jpeg')
cv2.imshow('birds',img)

def translate(img,x ,y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions =  (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)
#   -x --> left      , x--> right
#   -y -->up         y-->down
    
translated = translate(img, 100, 100)
cv2.imshow('translated',translated)

cv2.waitKey(0)
