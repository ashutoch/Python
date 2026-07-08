
#! Learning the difference btw list vs NumPy taking the population of Indian States as an example

#? Using Python list (manual loop)
population = [123, 455, 677, 776, 699]

# Find the avg population using a loop
total = 0
for pop in population:
    total = total + pop

average = total / len(population)
print(average)
# the problem with list is it can't handle large data sets as we need to pass the data through a loop which makes the calculation very slow and will also take a lot of memory as it is calculating the avg in every iteration as well as storing the data value simultaneously



#? Using NumPy (simpler and faster)
import numpy as np

# Direct average calculation
population_numpy = np.array([123, 455, 677, 776, 699])

average_np = np.mean(population_numpy)
print(average_np)