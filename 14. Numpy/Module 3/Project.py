
#! Image to Greyscale, Threshold convertor using NumPy

import numpy as py
from matplotlib.image import imread
import matplotlib.pyplot as plt



#* Step !: Load the image
#? imread -> converts the image into NumPy array (we do this because we are not loading the image as an image but rather a NumPy array because we are using numpy and it is also more efficient and also so we can apply some operations on it)

#? e.g.: (500, 700, 3) -> 500 rows (height), 700 columns (width), 3 channels (RGB)


image = imread(r"./Test.jpg")
print("image shape ", image.shape)

