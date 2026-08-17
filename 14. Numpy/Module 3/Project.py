
#! Image to Greyscale, Threshold convertor using NumPy

import numpy as py
from matplotlib.image import imread
import matplotlib.pyplot as plt



#* Step !: Load the image
#? imread -> converts the image into NumPy array (we do this because we are not loading the image as an image but rather a NumPy array because we are using numpy and it is also more efficient and also so we can apply some operations on it)

#? e.g.: (500, 700, 3) -> 500 rows (height), 700 columns (width), 3 channels (RGB)
# channel = pixels


image = imread(r"./Test.jpg")
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

