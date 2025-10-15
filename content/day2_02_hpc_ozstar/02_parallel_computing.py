#Lukas Steinwender
#%%imports
from joblib.parallel import Parallel, delayed
import logging
import numpy as np
import os
import sys
import time
from typing import Callable, List

DIR_PATH:str = os.path.dirname(os.path.realpath(__file__)) + "/"    #path to current directory
ROOT_PATH:str = f"{DIR_PATH}../../"                                 #path to project root
sys.path.append(ROOT_PATH)                                          #make sure root is visible to python

from cn5_pkg.cn5 import runtime_estimate

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

SLEEP:float = 0.25

#%%definitions
#task functions
def io_bound(x:float):
    """simulate I/O-bound work"""
    time.sleep(SLEEP)
    return x * 2

def cpu_bound(x:float):
    """simulate CPU-bound work (artificial computation)"""
    s = 0
    for i in range(300_000):
        s += (x * i) % 7
    return s

#different frameworks
def run_sequential(f:Callable, x:List):
    """
        - wrapper to run in sequential manner
    """
    res = []
    for xi in x:
        res.append(f(xi))
    return res

def run_parallel(f:Callable, x:List):
    """
        - wrapper to run in parallel manner (threading)
    """
    res = Parallel(n_jobs=-1, backend="threading", verbose=False)(delayed(f)(
        xi
    ) for xi in x)
    return res

@np.vectorize
def io_bound_vectorized(x:List):
    """
        - same as `io_bound()` except vectorized
    """
    time.sleep(SLEEP)
    return x * 2
@np.vectorize
def cpu_bound_vectorized(x:List):
    """
        - same as `cpu_bound()` except vectorized
    """
    s = 0
    for i in range(300_000):
        s += (x * i) % 7
    return s

#%%main
def main():
    x = np.arange(1,20)
    
    logger.info("I/O Bound")
    seq = runtime_estimate(run_sequential, io_bound,    x, nreps=1, nest=1, prefix="sequential: ")
    par = runtime_estimate(run_parallel, io_bound,      x, nreps=1, nest=1, prefix="parallel:   ")
    vec = runtime_estimate(io_bound_vectorized,         x, nreps=1, nest=1, prefix="vectorized: ")
    
    logger.info("CPU Bound")
    seq = runtime_estimate(run_sequential, cpu_bound,   x, nreps=1, nest=1, prefix="sequential: ")
    par = runtime_estimate(run_parallel, cpu_bound,     x, nreps=1, nest=1, prefix="parallel:   ")
    vec = runtime_estimate(cpu_bound_vectorized,        x, nreps=1, nest=1, prefix="vectorized: ")

if __name__ == "__main__":
    main()
