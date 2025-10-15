#Lukas Steinwender
#NOTE: to run with mpi call `mpiexec -n 4 python3 content/day2_02_hpc_ozstar/02_parallel_computing.py` from project root (mpi4py needs to be installed)

#%%imports
import datetime
from joblib.parallel import Parallel, delayed
import logging
import numpy as np
import os
import sys
import time
from typing import Callable, List, Literal

DIR_PATH:str = os.path.dirname(os.path.realpath(__file__)) + "/"    #path to current directory
ROOT_PATH:str = f"{DIR_PATH}../../"                                 #path to project root
sys.path.append(ROOT_PATH)                                          #make sure root is visible to python

from cn5_pkg.cn5 import runtime_estimate

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

SLEEP:float = 0.25

logger.info(f"available cores: {os.cpu_count()}")
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
    res = Parallel(n_jobs=4, backend="threading", verbose=False)(delayed(f)(
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

#mpi
def mpi_workers(MPI, comm, f:Callable, chunks:list):
    """
        - computations to be executed by the mpi workers
    """
    
    #assign local chunk to each worker
    x_local = comm.scatter(chunks, root=0)

    #compute
    t_start = MPI.Wtime()   #for timing
    res_local = np.array([f(xi) for xi in x_local])
    t_end = MPI.Wtime()     #for timing
    dt_local = t_end - t_start

    #gather results
    res_chunks = comm.gather(res_local, root=0)
        
    return res_chunks, dt_local

def run_mpi(MPI, f:Callable, x:List, setting:Literal["cpu","io"]="cpu"):
    """
        - function for running the script with mpi
            - when calling `mpiexec -n 4 python3 <scriptname.py>
    """
    comm = MPI.COMM_WORLD   #setup communicator
    rank = comm.Get_rank()  #get ranks
    size = comm.Get_size()  #get number of workers

    #init
    if rank == 0:
        #run other configs (just on controller to only run once)
        if setting=="io":
            logger.info("I/O Bound")
            seq = runtime_estimate(run_sequential, io_bound,    x, nreps=1, nest=1, prefix="sequential: ")
            par = runtime_estimate(run_parallel, io_bound,      x, nreps=1, nest=1, prefix="parallel:   ")
            vec = runtime_estimate(io_bound_vectorized,         x, nreps=1, nest=1, prefix="vectorized: ")
        elif setting=="cpu":    
            logger.info("CPU Bound")
            seq = runtime_estimate(run_sequential, cpu_bound,   x, nreps=1, nest=1, prefix="sequential: ")
            par = runtime_estimate(run_parallel, cpu_bound,     x, nreps=1, nest=1, prefix="parallel:   ")
            vec = runtime_estimate(cpu_bound_vectorized,        x, nreps=1, nest=1, prefix="vectorized: ")
        else:
            raise ValueError("`setting` has to be one of `'cpu'`, `'io'`")

        #prepare for mpi
        args = x
    else:
        args = None
    
    #split into roughly equal chunks
    if rank == 0:
        chunks = np.array_split(args, size)
    else:
        chunks = None
    
    if setting == "cpu":
        res_local, dt_local = mpi_workers(MPI, comm, cpu_bound, chunks)
    elif setting == "io":
        res_local, dt_local = mpi_workers(MPI, comm, io_bound, chunks)
    else:
        raise ValueError("`setting` has to be one of `'cpu'`, `'io'`")
    
    #gather results
    dt = comm.gather(dt_local, root=0)
    
    if rank == 0:
        dt_tot = max(dt)    #slowest worker dominates
        dt_tot = str(datetime.timedelta(seconds=dt_tot))
        logger.info(f"       mpi:        mean runtime over 1 executions: {dt_tot} => estimate for 1 executions: {dt_tot}")

        return None

#%%main
def main():
    x = np.arange(1,20)

    try:    #if mpi4py is installed, run with MPI 
        from mpi4py import MPI
        if MPI.COMM_WORLD.Get_size() == 1:
            logger.warning("MPI size of 1 => MPI setting equivalent to sequential")

        run_mpi(MPI, io_bound, x, "io")
        run_mpi(MPI, cpu_bound, x, "cpu")

    except ModuleNotFoundError as e:    #otherwise just standard python
        logger.info("ignoring mpi as `mpi4py` is not installed")
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
