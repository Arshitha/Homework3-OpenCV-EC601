# Homework3-OpenCV-EC601
Introductory Exercises on OpenCV

## Exercise 1
1. Matrix elements, in this case, pixels are stored row by row. Element(i,j) where i = 0 based row index and j = 0 based column index. However, before accessing the pixels we need to separate out the various channels. For instance, in an RGB image, the red, green and blue channels can be separated using the split function. To access the pixel values, the following command can be used *img.at<uchar>(Point(x, y))*.

## Exercise 2
1. **Comments on output:** 

   *Original Image* Displays the original image without any processing.
   
   *RGB Colorspace*
   
   *Red* Accesses and displays the red channel component of the original image.
   *Green* Acceses and displays the green channel component of the original image.
   *Blue* Accesses and displays the blue channel component of the original image.
   
   *YCbCr Colorspace*
   
   *Y* This is the luminance component of the original image. 
   *Cb and Cr* These are blue-difference and red-difference chroma components. "Cb and Cr are one representation of changes in     blue and red "colorfulness", respectively."
   [More info](https://stackoverflow.com/questions/17369660/what-do-blue-difference-and-red-difference-chroma-components-mean-in-ycbcr-color)
   
   *HSV Colorspace* 
   
   Similarly, the Hue, Saturation and Value components of the original image are displayed.
   
   Output and the python code are in the Exercise 2 folder.
   

2. The values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image are:

    **RGB value at (20,25) is  [106 122 225]**
    Each channel in the RGB colorspace ranges from 0-255.
  
    **YCbCr value at (20,25) is  [151 181 103]**
    Each channel in the YCbCr colorspace ranges from 0-255.
  
    **HSV value at (20,25) is  [  4 135 225]**
    HSV values range from [0,360] 
    
  
  
   
   
