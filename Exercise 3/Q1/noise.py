import numpy as np
import os
import cv2

def gaussian_noise(image, mean, sigma):
    row,col,ch= image.shape
    out = np.copy(image)
    mean = mean
    sigma = sigma
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    print ("\n")
    print (mean, sigma)
    print ("\n")
    noise_gauss = out + gauss
    print (noise_gauss)
    return noise_gauss

def salt_pepper_noise(image, salt, pepper):
    row,col,ch = image.shape
    amount_p = pepper*row*col
    amount_s = salt*row*col
    out = np.copy(image)
    for i in range(int(amount_s)):
        out[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))] = 255
    for i in range(int(amount_p)):
        out[int(np.random.uniform(0,row))][int(np.random.uniform(0,col))] = 0
    print ("\n")
    print ("pa = ", amount_s, "pb = ", amount_p)
    print ("\n")
    print (out)

    return out

def poisson_noise(image):
    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noise_pois = np.random.poisson(image * vals) / float(vals)
    return noise_pois


def speckle_noise(image):
    row,col,ch = image.shape
    gauss = np.random.randn(row,col,ch)
    gauss = gauss.reshape(row,col,ch)        
    noise_spec = image + image * gauss
    return noise_spec

if __name__ == "__main__":  
    Image = cv2.imread("Lenna.png")
    cv2.namedWindow("Original Image")
    cv2.imshow("Original Image",Image)
    cv2.imwrite("Image.jpg", Image)

    #Values of gaussian noise for different values of mean and variance
    Img1 = gaussian_noise(Image, 0, 0)
    Img2 = gaussian_noise(Image, 5, 20)
    Img3 = gaussian_noise(Image, 10, 50)
    Img4 = gaussian_noise(Image, 20, 100)

    #Filters on gaussian noise images
    cv2.namedWindow("Gaussian Noise Image(10,50)")
    cv2.imshow("Gaussian Noise Image",Img3)
    cv2.imwrite("GaussImage.jpg", Img3)

    #Box filter
    noise_dst=Img3.copy()
    cv2.blur(noise_dst,(3,3))
    cv2.imshow('Box Filter (3,3)', noise_dst)     
    cv2.imwrite('BoxFilter33.png', noise_dst)

    cv2.blur(noise_dst,(5,5))
    cv2.imshow('Box Filter (5,5)', noise_dst)     
    cv2.imwrite('BoxFilter55.png', noise_dst)

    cv2.blur(noise_dst,(7,7))
    cv2.imshow('Box Filter (7,7)', noise_dst)     
    cv2.imwrite('BoxFilter77.png', noise_dst)

    #Gaussian filter
    noise_dst1=Img3.copy()
    cv2.GaussianBlur(noise_dst1,(3,3),1.5)
    cv2.imshow('Gaussian Filter', noise_dst1)      
    cv2.imwrite('GaussianFilter.png', noise_dst1)

    #Median filter
    """noise_dst2=Img3.copy()
    cv2.medianBlur(noise_dst2,3)
    cv2.imshow('Median Filter', noise_dst2)     
    cv2.imwrite('MedianFilter.png', noise_dst2)"""

    #Values of salt-pepper noise at different values of pa and pb
    spImg1 = salt_pepper_noise(Image, 0.01, 0.01)
    spImg2 = salt_pepper_noise(Image, 0.03, 0.03)
    spImg3 = salt_pepper_noise(Image, 0.05, 0.05)
    spImg4 = salt_pepper_noise(Image, 0.4, 0.4)

    #Filters on salt pepper noise images
    cv2.namedWindow("Salt and Pepper Noise Image (0.01,0.01)")
    cv2.imshow("Salt&Pepper Noise Image",spImg1)
    cv2.imwrite("SaltPepperImage.jpg", spImg1)

    #Box Filter
    noise_dst3=spImg1.copy()
    cv2.blur(noise_dst3,(3,3))
    cv2.imshow('Box Filter', noise_dst3)
    cv2.imwrite('BoxFilter2.png', noise_dst3)

    #Gaussian Filter
    noise_dst4=spImg1.copy()
    cv2.GaussianBlur(noise_dst4,(3,3),1.5)
    cv2.imshow('GaussianBlur Filter', noise_dst4)
    cv2.imwrite('GaussianFilter2.png', noise_dst4)

    #Median Filter
    noise_dst5=spImg1.copy()
    cv2.medianBlur(noise_dst5,3)
    cv2.imshow('Median Filter', noise_dst5)
    cv2.imwrite('MedianFilter2.png', noise_dst5)

    #Poisson Noise and Speckle Noise
    poi_noise_img = poisson_noise(Image)
    spec_noise_img = speckle_noise(Image)
    cv2.namedWindow("Poisson Noise Image")
    cv2.imshow("Poisson Noise Image",poi_noise_img)
    cv2.imwrite("PoissonImage.jpg", poi_noise_img)

    cv2.namedWindow("Speckle Noise Image")
    cv2.imshow("Speckle Noise Image",spec_noise_img)
    cv2.imwrite("SpeckleImage.jpg", spec_noise_img)