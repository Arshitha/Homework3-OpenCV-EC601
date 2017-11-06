import cv2
import numpy as np

OriImg = cv2.imread("Lenna.png")

cv2.NamedWindow("Original Image")
cv2.imshow("Original Image",OriImg)
cv2.imwrite("Image.jpg", OriImg)

blue, green, red = cv2.split(OriImg)

