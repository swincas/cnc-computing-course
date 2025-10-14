#Lukas Steinwender

#%%imports
import logging
import numpy as np
from datetime import datetime
from typing import Callable
from utils import runtime_estimate

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

#%%definitions
def arr_sum(n:int=10000):
    """
        - computes sum of two large arrays (size `(n,n)`)
    """
    #estimate memory usage of this array
    #estimate how long it takes to create
    big_arr_1 = np.ones((n,n))
    big_arr_2 = np.full_like(big_arr_1, 2)

    sum = np.sum(big_arr_1) + np.sum(big_arr_2)

    logger.info(f"Sum of large array: {sum}")
    return

#%%main
def main():
    runtime_estimate(arr_sum, 10000, nreps=3, nest=10)

if __name__ == "__main__":
    main()

