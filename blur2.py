import cv2
img= cv2.imread("images/OIP.jpeg")

cv2.imshow("image",img)

#Averaging
average= cv2.blur(img,(7,7))
cv2.imshow("average",average)

#gaussian blur
gauss = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('gaussian blur',gauss)

#median blur
median = cv2.medianBlur(img,3)
cv2.imshow('median blur',median)
#bilateral 
bilat= cv2.bilateralFilter(img,10,35,35)
cv2.imshow("bilateral",bilat)
cv2.waitKey(0)
