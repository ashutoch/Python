
#! Random Module in NumPy
# numpy.random is very useful for AI, ML and simulations

#* Random Numbers
import numpy as np

#* Random float (0 to 1) 
# print(np.random.rand(3))  #? inside the bracket we write the number of data that we want, here we want 3 random numbers so we wrote 3

#* 5 Random integers (1 to 9)
# print(np.random.randint(1, 9, 5))   #? (minimum, maximum, number of data) also it never selects the max value 

#* 2D Random Array
arr = np.random.randint(1, 100, (3, 3))     #? (minimum, maximum, shape)
print(arr)