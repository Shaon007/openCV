import cv2
import numpy as np
img = cv2.imread("images/R1.jpg")
imgResize = cv2.resize(img,(50,50))
#img[:,:,0]=0    #bgr color values conv to 0, 0=blue, 1=green, 2=red
#cv2.imshow("window",img)

imgBlue = imgResize [:,:,0]
imgGreen = imgResize[:,:,1]
imgRed = imgResize[:,:,2]
new_img = np.hstack((imgBlue, imgGreen, imgRed)) #showing all 3 img side by side
cv2.imshow("window",new_img)
cv2.waitKey(0)

