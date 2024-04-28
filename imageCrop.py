import cv2
img = cv2.imread("images/OIP.jpeg")

img_crop = img[100:300, 200:500]
cv2.imshow("birds",img_crop)
cv2.waitKey(0)
