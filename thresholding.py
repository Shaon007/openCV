import cv2
 
img= cv2.imread('images/OIP.jpeg')

cv2.imshow('birds',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
#simple thresholding
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',thresh)     # value changes black white lvl

threshold, thresh_inv = cv2.threshold(gray, 150, 250, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh inverse',thresh_inv)

#adaptive thresholding
adaptive_thresh= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow('Adaptive Thresh',adaptive_thresh)

adaptive_thresh_inv= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,3)
cv2.imshow('Adaptive Thresh inv',adaptive_thresh_inv)

cv2.waitKey(0)
