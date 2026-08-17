
#! Image to Greyscale, Threshold convertor using NumPy

import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt



#* Step !: Load the image
#? imread -> converts the image into NumPy array (we do this because we are not loading the image as an image but rather a NumPy array because we are using numpy and it is also more efficient and also so we can apply some operations on it)

#? e.g.: (500, 700, 3) -> 500 rows (height), 700 columns (width), 3 channels (RGB)
# channel = pixels


image = imread(r"D:\Project_and_Codes\Python\14. Numpy\Module 3\Test.jpg")
print("image shape ", image.shape)

#! greyscale = (0.2989 * R) + (0.5870 * G) + (0.1140 * B)
#! threshold = 0 and 255



#* Step 2: Extract the RGB channels
#NumPy concept here: Indexing and slicing

R = image[ : , : , 0]
G = image[ : , : , 1]
B = image[ : , : , 2]



#* Step 3: Convert to Greyscale 
# NumPy concept here: Broadcasting and element-wise operation

greyscale = (0.2989 * R) + (0.5870 * G) + (0.1140 * B)
print(" GreyScale shape ", greyscale)



#* Step 4: Apply Threshold
# syntax : np.where(condition, value_if_true, value_if_false)
# np.where(condition, value_if_true, value_if_false)

threshold_value = 128
threshold = np.where(greyscale > threshold_value, 255, 0)


#* Step 5: Display the result

plt.figure(figsize = (12, 4))

plt.subplot(1, 3, 1)    # 1 at the end for the original image to be placed at the start
plt.title("original")
plt.imshow(image.astype(np.uint8))

plt.subplot(1, 3, 2)    # 2 at the end for the greyscale image to be placed at 2nd position
plt.title("greyscale")
plt.imshow(greyscale, cmap = "gray")    # cmap tells the compiler that the image is in greyscale and to print it as such


plt.subplot(1, 3, 3)    # 3 at the end for the threshold image to be placed at 3rd position
plt.title("threshold")
plt.imshow(threshold, cmap = "gray")


plt.tight_layout()  # prevents the images from overlapping and also helps to space them evenly

plt.show()





# plt.subplot(1, 3, n) : display 3 images in a row

# astype(np.uint8) : converts pixel values into integers (0 - 255)

# plt.figure(figsize = (12, 4)) #? Purpose : Creates a new figure/canvas to plot your image

# figsize = (width, height) : defines the size of the figure in inches

# plt.subplot(1, 3, 1) #? Purpose: divide the figure into a grid and select the cell to plot in 
#? Syntax: plt.subplot(nrows, ncols, index)