#Lukas Steinwender

#%%imports
import numpy as np
from datetime import datetime
from typing import Callable

#%%definitions
def runtime_estimate(f:Callable, nreps:int=1, nest:int=10, *args):
    """
        - estimate runtime of `f(*args)` over `nreps` executions
        - project estimate to `nest` executions
    """
    
    #do `nreps` repetitions
    durations = []
    for _ in range(nreps):
        start = datetime.now()  #starting time of current execution

        f(*args)    #run function
        end = datetime.now()    #completion time of current execution
        durations.append(end-start)
    
    rt_est = np.mean(durations)
    print(f"mean runtime over {nreps} executions: {rt_est} => estimate for {nest} executions: {rt_est*nreps}")
    return 

def arr_sum(n:int=10000):
    """
        - computes sum of two large arrays (size `(n,n)`)
    """
    #estimate memory usage of this array
    #estimate how long it takes to create
    big_arr_1 = np.ones((n,n))
    big_arr_2 = np.full_like(big_arr_1, 2)

    sum = np.sum(big_arr_1) + np.sum(big_arr_2)

    print(f"Sum of large array: {sum}")
    return

#%%main
def main():
    runtime_estimate(arr_sum, 3, 10, 10000)

if __name__ == "__main__":
    main()

