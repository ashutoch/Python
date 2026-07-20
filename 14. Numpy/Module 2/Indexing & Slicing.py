import numpy as np

#! Basic Indexing

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])


#! Multi-dimensional indexing
# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr_2d[1, 2])

#! Advanced Indexing / Boolean
# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
# print(arr[arr > 50])


#! Slicing
# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
# print(arr[1 : 3])

#? Full Slice (Copy of an array)
# print( arr[ : ] )

#? Step Slicing
# print(arr[: : 2])

#? Reverse Array
# print(arr[ : : -1])



#! Examples
#? Slice first two rows and first 3 columns 

# arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(arr2d[ : 2, : 3])

#? Slice all rows and all columns
# print(arr2d[ : , : ])

#? SLice the last 2 rows and last 2 columns
# print(arr2d[1: , 2:])



#! Advanced Slicing
#? Selecting alternate rows
# arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(arr2d[ : : 2, : ])


#? Selecting alternate columns
# print(arr2d[ : , : : 2])


#? Cropping (like image cropping, i,e., square shape)
# print(arr2d[0:2, 1:3])


#? Reversing the rows
# print(arr2d[ : : -1, : ])


#? Reversing the columns
# print(arr2d[ : , : : -1])


#? Reversing the whole array
# print(arr2d[ : : -1, : : -1])