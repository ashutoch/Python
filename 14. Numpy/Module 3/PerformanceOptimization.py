
#! Performance Optimization is highly used in Data Science Preprocessing

#? First lets try to compare loop vs vectorization speed

import time
import numpy as np

arr = np.arange(1, 100000001)

#* Using Loop

start1 = time.time()
square1 = [x**2 for x in arr]
end1 = time.time()
print(end1 - start1)

#* Using Vectorization

start2 = time.time()
square2 = arr ** 2
end2 = time.time()
print(end2 - start2)