import numpy as np

#! Using Python Loop

# scores = [50, 10, 30, 60, 90, 70, 20, 40]

#? add 5 bonus marks into the scores array using loop

# bonus = []
# for s in scores:
#     bonus.append(s + 5)
# print(bonus)


#! Using Numpy
#* Instead of looping we can directly add a scalar (single value) to a NumPy array & NumPy automatically broadcasts the value to match the array's shape

# scores = np.array([50, 10, 30, 60, 90, 70, 20, 40])
# bonus = scores + 5
# print(bonus)


#! Broadcasting between different shapes
#* Suppose we have 2D data of students marks

marks = np.array([[50, 10, 30, 60], [90, 70, 20, 40], [88, 95, 77, 67]])

#? we want to add grace marks [2, 3, 4, 5] for each row respectively

grace = np.array([2, 3, 4, 5])

result = marks + grace
print(result)