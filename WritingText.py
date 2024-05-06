import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('blank',blank)

cv2.putText(blank, 'Shaon',(225,225),cv2.FONT_HERSHEY_TRIPLEX, 1.0, (200,100,0),2)
cv2.imshow('text',blank)

cv2.waitKey(0)
