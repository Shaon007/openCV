import cv2

img = cv2.imread("images\R1.jpg",0)

cv2.imshow("Flowers",img)
cv2.waitKey(0)
