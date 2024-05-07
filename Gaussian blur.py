import cv2
import numpy as np

img = cv2.imread('images/OIP.jpeg')
cv2.imshow('Birds',img)

blur = cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
                      # blur level( must be odd num)
cv2.imshow("blurr",blur)

cv2.waitKey(0)
