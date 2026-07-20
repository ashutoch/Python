import numpy as np

#? Python list vs NumPy array
list_data = [1, 2, 3, 4, 5, 6.9]
print(list_data)
print(type(list_data))

array_data = np.array([1, 2, 3, 4, 5, 6.9])
print(array_data)
print(type(array_data))
# in the above arrays we mixed integers and floats together
# NumPy always converts the entire array into a single data type for effeciency

array_data2 = np.array([1, 2, 3, 4, 5, 6.9], dtype = int)
print(array_data2)
print(type(array_data2))
# this forcefully converts all the data to int data type
