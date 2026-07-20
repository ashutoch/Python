import numpy as np

#! Creating arrays from python lists

arr = np.array([1, 2, 3, 4, 5])



#! Using built-in functions in numpy
#! Zeros Array

# zeros_array = np.zeros(5)     # 1D array of 0s
# zeros_array2 = np.zeros([2, 3])     # 2D array of 0s
# zeros_array3 = np.zeros([2, 2, 3])     # 3D array of 0s
# print(zeros_array)
# print(zeros_array2)
# print(zeros_array3)


#! Ones Array
# ones_array = np.ones(5)
# print(ones_array)

#? these type of function is used when we want to assign some placeholder value to an array which will be updated or changed later by the user



#! Constant / Full Array

# constant_arr = np.full((3, 3), 15)
# print(constant_arr)

#? this function fills the matrix with the value which is given inside its parameters



#! Identity Matrix
## identity_arr = np.eye(3, 3)
# identity_arr = np.eye(3)

# print(identity_arr)

#? Inserts the data diagonally



#! Range Array
# range_arr = np.arange(0, 10, 2)
# print(range_arr)

#? arange(start, stop, steps)
#? works only for 1D array



#! Linespace Array
lines = np.linespace(0, 1, 5)
print(lines)

#? np.linespace(start, stop, pieces)
#? here pieces signify the number of divisions