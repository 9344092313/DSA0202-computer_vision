#image rotation
import cv2


path = "C:/Users/heman/OneDrive/Desktop/image.jpg"


src = cv2.imread(path)


window_name = 'Image'


image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)


cv2.imshow(window_name, image)
cv2.waitKey(0)
