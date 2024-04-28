import cv2

img = cv2.imread("images/OIP.jpeg")
img_flip = cv2.flip(img,-1)
cv2.imshow("window",img_flip)
cv2.waitKey(0)
