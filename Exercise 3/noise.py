import numpy as np
import os
import cv2

def gaussian_noise(image, mean, sigma):
    row,col,ch= image.shape
    mean = mean
    #var = var
    sigma = sigma
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    print ("\n")
    print (mean, sigma)
    print ("\n")
    print (gauss)
    noise_gauss = image + gauss
    return noise_gauss

def salt_pepper_noise(image, salt, pepper):
    row,col,ch = image.shape
    amount_p = pepper
    amount_s = salt
    s_vs_p = 0.5
    out = np.copy(image)
    #Salt mode
    num_salt = np.ceil(amount_s * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 255
    
    # Pepper mode
    num_pepper = np.ceil(amount_p* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    
    out[coords] = 0
    print ("\n")
    print ("pa = ", amount_s, "pb = ", amount_p )
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

    Img1 = gaussian_noise(Image, 0, 0)
    Img2 = gaussian_noise(Image, 5, 20)
    Img3 = gaussian_noise(Image, 10, 50)
    Img4 = gaussian_noise(Image, 20, 100)

    
    spImg1 = salt_pepper_noise(Image, 0.01, 0.01)
    spImg2 = salt_pepper_noise(Image, 0.03, 0.03)
    spImg3 = salt_pepper_noise(Image, 0.05, 0.05)
    spImg4 = salt_pepper_noise(Image, 0.4, 0.4)


    poi_noise_img = poisson_noise(Image)
    spec_noise_img = speckle_noise(Image)

    cv2.namedWindow("Gaussian Noise Image")
    cv2.imshow("Gaussian Noise Image",Img3)
    cv2.imwrite("GaussImage.jpg", Img3)

    cv2.namedWindow("Salt and Pepper Noise Image (0.01,0.01)")
    cv2.imshow("Salt&Pepper Noise Image",spImg1)
    cv2.imwrite("SaltPepperImage.jpg", spImg1)

    cv2.namedWindow("Poisson Noise Image")
    cv2.imshow("Poisson Noise Image",poi_noise_img)
    cv2.imwrite("PoissonImage.jpg", poi_noise_img)

    cv2.namedWindow("Speckle Noise Image")
    cv2.imshow("Speckle Noise Image",spec_noise_img)
    cv2.imwrite("SpeckleImage.jpg", spec_noise_img)