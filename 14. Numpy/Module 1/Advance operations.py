
#? np.append() is used to add values to an array
#? it creates a new array with the added elements

import numpy as np

# arr = np.array([1, 2, 3])
# new = np.append(arr, 4)

# print(new)

#! Multidimensional Example

#? Append row
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# new = np.append(arr, [[7, 8, 9]], axis=0)
# for x axis the value is 0 and for y axis the value is 1
# print(new)


#? Append column
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# new = np.append(arr, [[7], [8]], axis=1)
# print(new)


#! Concatinating arrays
# np.concatenate() joins arrays along the existing axis

#? 1D array
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.concatenate((a, b))
# print(c)

#? Multidimenional array
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])
#* for row
# z = np.concatenate((x, y), axis=0)

#* for column
# z = np.concatenate((x, y), axis=1)

# print(z)


#? 2D array

#* along rows
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6]])
# z = np.concatenate((x, y), axis=0)

# print(z)

#* along columns
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5], [6]])
# z = np.concatenate((x, y), axis=1)

# print(z)


#! Insert Elements
#? np.insert(): inserts values at specified position (index number)

# arr = np.array([1, 2, 5])

#* for 1 element
# new = np.insert(arr, 2, 3)  # (array, index, value)
# print(new)

#* for more than 1 element
# new = np.insert(arr, 2, [3, 4])

# new = np.insert(arr, (2, 3), (3, 4))
# print(new)


#? 2D example
#* for row -> axis = 0, for column -> axis = 1

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# # new = np.insert(arr, 1, [9, 9])
# new = np.insert(arr, 1, [9, 9], axis = 1)

# print(new)



#! Delete Elements
#? np.delete() removes elements from the array

#* delete index 2
#? for 1D array
# arr = np.array([1, 2, 3, 4, 5])
# new = np.delete(arr, 2)
# print(new)

#? for 2D array
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# new = np.delete(arr, 1, axis = 0)   #* for row
# new = np.delete(arr, 1, axis = 1)   #* for column
# print(new)




#! Splitting arrays
