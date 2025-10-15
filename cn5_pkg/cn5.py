"""
    - utilities used in scripts in day2_02_hpc_ozstar/
    - author: Lukas Steinwender
"""
#%%imports
from datetime import datetime
import logging
import numpy as np
import os
from typing import Callable

logger = logging.getLogger(__name__)

#%%definitions
def runtime_estimate(f:Callable, *args, nreps:int=1, nest:int=10, prefix:str=None):
    """
        - estimate runtime of `f(*args)` over `nreps` executions
        - project estimate to `nest` executions
        - adds `prefix` to output message
    """
    
    #default parameters
    if prefix is None: prefix = ""

    #do `nreps` repetitions
    durations = []
    for _ in range(nreps):
        start = datetime.now()  #starting time of current execution

        f(*args)    #run function
        end = datetime.now()    #completion time of current execution
        durations.append(end-start)
    
    rt_est = np.mean(durations)
    logger.info(f"{prefix}mean runtime over {nreps} executions: {rt_est} => estimate for {nest} executions: {rt_est*nreps}")
    return 

def makefile(filepath:str, force:bool=False):
    """
        - creates a new file
        - if `force==True`: will overwrite any existing file of the same name
        - if `force==False`: will only create a new file if it is not yet existing
    """
    
    if not os.path.exists(filepath) or force:   #onlyif `force` or file not yet existent
        open(filepath, "w").close()             #create new, empty file

    return