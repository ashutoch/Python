import numpy as np
#! Splitting arrays

#* np.split(), np.hsplit(), np.vsplit()

# arr = np.array([1, 2, 3, 4, 5, 6])
# new = np.split(arr, 3)
# print(new)

# a1, a2, a3 = np.split(arr, 3)
# print(a1, a2, a3)


#! Horizontal Split
#? np.hsplit(arr2d, 2) means: split the array into 2 parts along the column (axis = 1)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# a1, a2 = np.hsplit(arr, 2)
# print(a1, a2)


#! Vertical Split
#? np.vsplit(arr2d, 2) means: split the array into 2 parts along the row (axis = 0)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# a1, a2 = np.vsplit(arr, 2)
# print(a1, a2)



#! Stacking
#* np.stack(), np.hstack(), np.vstack()


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.stack((a, b)))
# print(np.hstack((a, b)))
# print(np.vstack((a, b)))



