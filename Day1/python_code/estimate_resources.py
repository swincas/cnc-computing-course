# imports
import numpy as np

# estimate memory usage of this array
# estimate how long it takes to create
big_arr_1 = np.ones((100000,100000))
big_arr_2 = np.full_like(big_arr_1, 2)

sum = np.sum(big_arr_1) + np.sum(big_arr_2)

print(f"Sum of large array: {sum}")




