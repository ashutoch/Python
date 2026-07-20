
#! Array Attributes
# import numpy as np

# array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(array_2d)

# print(array_2d.shape)   #? columns & rows
# print(array_2d.ndim)    #? dimensions
# print(array_2d.size)    #? total size of the array
# print(array_2d.dtype)   #? data type of the array


#! Changing data type
# float_data = array_2d.astype(float)
# print(float_data)

# float_data[0] = 95.5
# print(float_data)

#? Indexing:
#? float_data[0] -> the entire first row of the matrix (3 x 4)
#? float_data[0, 0] -> the first element of the first column


#! Reshaping array
# newShape = array_2d.reshape(2, 6)
# print(newShape)

# import numpy as np
# reshaping_arr = np.arange(6).reshape(2, 3)
# print(reshaping_arr)


#! Flattening arrays
#? converting 2D arrays into 1D arrays

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.flatten())