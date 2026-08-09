
#! Performance Optimization is highly used in Data Science Preprocessing

#? First lets try to compare loop vs vectorization speed

import time
import numpy as np

arr = np.arange(1, 10000001)

#* Using Loop

start = time.time()
square = [x**2 for x in arr]
end = time.time()
print(end - start)

#* Using Vectorization