import cv2
import numpy as np

OriImg = cv2.imread("Lenna.png")

cv2.NamedWindow("Original Image")
cv2.imshow("Original Image",OriImg)
cv2.imwrite("Image.jpg", OriImg)

print("RGB value at (20,25) is ",OriImg[20,25])
print("YCbCr value at (20,25) is ", OriImg[])