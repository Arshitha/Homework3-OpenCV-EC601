import cv2
import numpy as np

OriImg = cv2.imread("Lenna.png")

cv2.NamedWindow("Original Image")
cv2.imshow("Original Image",OriImg)
cv2.imwrite("Image.jpg", OriImg)

blue, green, red = cv2.split(OriImg)

cv2.NamedWindow("Blue")
cv2.imshow("Blue", blue)
cv2.imwrite("Blue.jpg", blue)

cv2.NamedWindow("Green")
cv2.imshow("Green", green)
cv2.imwrite("Green.jpg", green)

cv2.NamedWindow("Red")
cv2.imshow("Red", red)
cv2.imwrite("Red.jpg", red)




