import numpy as np
import os
import cv2

def gaussian_noise(noise_typ,image, mean, var):
    
    row,col,ch= image.shape
    mean = mean
    var = var
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy
    
def salt_pepper_noise(image, salt, pepper)
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    out = np.copy(image)
    #Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1

if __name__ == "__main__":
    Image = cv2.imread("Lenna.png")

    cv2.namedWindow("Original Image")
    cv2.imshow("Original Image",Image)
    cv2.imwrite("Image.jpg", Image)

    guass_noise_img = noisy("gauss", Image, 10, 50 )
    cv2.namedWindow("Gaussian Noise Image")
    cv2.imshow("Gaussian Noise Image",guass_noise_img)
    cv2.imwrite("GaussImage.jpg", guass_noise_img)
    