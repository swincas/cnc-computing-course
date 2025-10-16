#%%imports
import logging
import numpy as np
from cn5_pkg import cn5

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

#%%definitions
def row_index(a:np.ndarray):
    """
        - demonstrates row indexing
    """
    N1, N2 = a.shape
    for i in range(N1):
        _ = a[i,:].sum()    #access row
    return
def col_index(a:np.ndarray):
    """
        - demonstrates column indexing
    """    
    N1, N2 = a.shape
    for j in range(N2):
        _ = a[:,j].sum()    #access row
    return
def copying(a:np.ndarray, copy:bool=True):
    """
        - demonstrates copying vs referencing, views
    """    
    
    if copy:
        b = a.copy()    #copy
    else:
        b = a           #reference
    print(f"{copy=}")
    print(f"`a` input:                     {a}")
    b = b[0:3]          #view
    b *= 4
    print(f"`a` after modification of `b`: {a}")
    return
def manipulation(a:np.ndarray):
    """
        - demonstrates some manipulations
    """    
    #reshapeing
    a_r = a.reshape(5,2,-1)
    print(a_r.shape, a_r)
    #transposing (switching dimensions)
    a_t = a_r.transpose((1,2,0))
    print(a_t.shape, a_t)
    #matrix products
    b = a.reshape(5,-1)
    print((b.T@b).shape)
    #einsum
    c = np.einsum("ijk,ijk -> ik", a_r, a_r)
    print(c.shape)

    return

#%%main
def main():
    N = 5000
    a = np.random.rand(N,N)

    #warmup (avoid first time overheads)
    _ = a[0,:].sum()
    _ = a[:,0].sum()
    
    cn5.runtime_estimate(row_index, a, nreps=20, nest=1, prefix="row_index")
    cn5.runtime_estimate(col_index, a, nreps=20, nest=1, prefix="col_index")
    
    copying(np.arange(0,10), copy=False)
    copying(np.arange(0,10), copy=True)

    manipulation(np.arange(0,20))

if __name__ == "__main__":
    main()