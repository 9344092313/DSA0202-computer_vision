import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("C:/Users/heman/Downloads/download.jpg", cv2.IMREAD_COLOR)
#small image

#img = cv2.resize(img,(50,50))
#enlarged image
#img = cv2.resize(img,(300,300))

img = cv2.resize(img,(1200,800))



cv2.imshow("image", img)



cv2.waitKey(0)
