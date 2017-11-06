import cv2
import numpy as np

OriImg = cv2.imread("Lenna.png")

cv2.namedWindow("Original Image")
cv2.imshow("Original Image",OriImg)
cv2.imwrite("Image.jpg", OriImg)

print("RGB value at (20,25) is ",OriImg[20,25])

ImgYC = cv2.cvtColor(OriImg, cv2.COLOR_BGR2YCrCb)

print("YCbCr value at (20,25) is ",ImgYC[20,25])

ImgHSV = cv2.cvtColor(OriImg, cv2.COLOR_BGR2HSV)

print("HSV value at (20,25) is ",ImgHSV[20,25])

