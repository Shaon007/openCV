import cv2
import numpy as np
#img= cv2.imread("images/OIP.jpeg")
#cv2.imshow("image",img)

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv2.circle(blank.copy(),(200,200),200,255,-1)

cv2.imshow('rectangle', rectangle)
cv2.imshow('circle',circle)

#bitwise
bitwise_and = cv2.bitwise_and (rectangle, circle)
cv2.imshow('Bitwise and',bitwise_and)

#bitwise or
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('bitwise or', bitwise_or)

#bitwise xor
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('bitwise xor',bitwise_xor)

#bitwise not
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow("bitwise not", bitwise_not)

cv2.waitKey(0)
