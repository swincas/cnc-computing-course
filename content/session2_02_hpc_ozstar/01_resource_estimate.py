#Lukas Steinwender

#%%imports
import logging
import numpy as np
import os
import sys

DIR_PATH:str = os.path.dirname(os.path.realpath(__file__)) + "/"    #path to current directory
ROOT_PATH:str = f"{DIR_PATH}../../"                                 #path to project root
sys.path.append(ROOT_PATH)                                          #make sure root is visible to python

from cn5_pkg.cn5 import runtime_estimate

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

