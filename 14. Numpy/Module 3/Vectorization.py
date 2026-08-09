import numpy as np

#! Vectorization (fast operation)
#* Vector means replacing the loop with array operations (+, -, *, /, %, ** etc), which makes the code shorter, cleaner and thousand of times faster

#* Example: Calculate the square of 10 lakh members
arr = np.arange(1, 1000001)

#? Loop method

squared = [x**2 for x in arr]
print(squared)

#? Vectorized method
square = arr ** 2
print(square)   # the full answer is already fetched in the background


