import numpy as np

#? Basics of arrays
# arrays are helpful when we try to store large amount of data

# d1 = 123
# d2 = 4555
# d3 = 5678
# arr = [123, 4555, 5678]

#! NumPy Arrays
#? Creating a 1D array from a list

# array_1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# print(array_1D)
# print(type(array_1D))

# print(array_1D.shape)
# prints only (10,) here because the differentiating thing here is the number of columns as the row is basically 1 only

#! Shape = [no. of rows, no. of columns]



#? Creating a 2D array from a list of lists

# array_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(array_2D)
# print(array_2D.shape)


#? Creating a 3D array 
# A cube with multiple 2D arrays inside it


array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array_3D)
print(array_3D.shape)

#! Shape = [no. of blocks, no. of rows, no. of columns]
