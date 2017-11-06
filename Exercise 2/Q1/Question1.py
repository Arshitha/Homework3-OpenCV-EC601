import cv2
import numpy as np

OriImg = cv2.imread("Lenna.png")

cv2.namedWindow("Original Image")
cv2.imshow("Original Image",OriImg)
cv2.imwrite("Image.jpg", OriImg)

blue, green, red = cv2.split(OriImg)

cv2.namedWindow("Blue")
cv2.imshow("Blue", blue)
cv2.imwrite("Blue.jpg", blue)

cv2.namedWindow("Green")
cv2.imshow("Green", green)
cv2.imwrite("Green.jpg", green)

cv2.namedWindow("Red")
cv2.imshow("Red", red)
cv2.imwrite("Red.jpg", red)

ImgYC = cv2.cvtColor(OriImg, cv2.COLOR_BGR2YCrCb)
Y, Cb, Cr = cv2.split(ImgYC)

cv2.namedWindow("Y")
cv2.imshow("Y", Y )
cv2.imwrite("Y.jpg", Y)

cv2.namedWindow("Cb")
cv2.imshow("Cb", Cb)
cv2.imwrite("Cb.jpg", Cb)

cv2.namedWindow("Cr")
cv2.imshow("Cr", Cr)
cv2.imwrite("Cr.jpg", Cr)



ImgHSV = cv2.cvtColor(OriImg, cv2.COLOR_BGR2HSV)
Hue, Sat, Val = cv2.split(ImgYC)

cv2.namedWindow("Hue")
cv2.imshow("Hue", Hue )
cv2.imwrite("Hue.jpg", Hue)

cv2.namedWindow("Sat")
cv2.imshow("Sat", Sat)
cv2.imwrite("Sat.jpg", Sat)

cv2.namedWindow("Val")
cv2.imshow("Val", Val)
cv2.imwrite("Val.jpg", Val)


