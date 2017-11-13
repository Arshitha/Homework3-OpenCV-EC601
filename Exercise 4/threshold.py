import cv2
import numpy as np
import sys


if __name__ == "__main__":
    image = cv2.imread("Lenna.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    [cv, threshold] = cv2.threshold(gray, 128, 255, 2)
    cv2.imshow('Threshold', threshold)

    [cv, binThreshold] = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    cv2.namedWindow("Binary Threshold")
    cv2.imshow('Binary Threshold', binThreshold)
    cv2.imwrite("BinThreshold.jpg", binThreshold)

    [cv, threshold1] = cv2.threshold(gray, 27, 255, cv2.THRESH_BINARY)
    [cv, threshold2] = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
    BandThreshold = cv2.bitwise_and(threshold1, threshold2)
    cv2.namedWindow("Band Threshold")
    cv2.imshow('Band Threshold', BandThreshold)
    cv2.imwrite("BandThreshold.jpg", BandThreshold)

    [cv, threshold3] = cv2.threshold(
        gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    semiThreshold = cv2.bitwise_and(gray, threshold3)
    cv2.namedWindow("Semi Threshold")
    cv2.imshow('Semi Threshold', semiThreshold)
    cv2.imwrite("SemiThreshold.jpg", semiThreshold)

    AdapThreshold = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
    cv2.namedWindow("Adaptive Threshold")
    cv2.imshow('Adaptive Threshold', AdapThreshold)
    cv2.imwrite("AdaptiveThreshold.jpg", AdapThreshold)    