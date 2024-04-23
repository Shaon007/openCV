import cv2
img = cv2.imread("images\DIP3E_Original_Images_CH01\Fig0107(b)(kidney-original).tif",0)

img_resize = cv2.resize(img,(200,200))
cv2.imshow('image',img_resize)
print(img_resize.shape)
cv2.waitKey(0) 

