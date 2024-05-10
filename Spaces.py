import cv2
import numpy as np

img = cv2.imread('images/OIP.jpeg')
cv2.imshow('birds',img)

#BGR to H.S.V. (hue, saturation, value)
hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
#BGR to L.A.B.  (Lightness; Axis of gren ,red ; Blue Yellow axis)
lab= cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
cv2.waitKey(0)
