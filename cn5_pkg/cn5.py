"""
    - utilities used in the course
    - might be useful for participants' research as well
    - author: Lukas Steinwender
"""
#%%imports
from cycler import cycler
from datetime import datetime, timedelta
import logging
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
from typing import Callable, List, Tuple, Union

logger = logging.getLogger(__name__)

#%%definitions
def runtime_estimate(
    f:Callable, *args, nreps:int=1, nest:int=10, prefix:str=None
    ) -> Tuple[timedelta, timedelta]:
    """
        - estimate runtime of `f(*args)` over `nreps` executions
        - project estimate to `nest` executions
        - adds `prefix` to output message

        Parameters
        ----------
            - `f`
                - `Callable`
                - function to be timed
            - `*args`
                - `Any`
                - arguments to be passed to `f`
            - `nreps`
                - `int`, optional
                - number of times to evaluate `f(*args)`
                - runtime estimate will be the mean across all executions
                - the default is `1`
            - `nest`
                - `int`, optional
                - number of runs to estimate the duration for
                - will project result from `nreps` evaluations onto `nest` function calls
                - the default is `10`
            - `prefix`
                - `str`, optional
                - prefix for the report
                - usually the function name or context
                - the default si `None`
                    - will be set to `""`
                    - no prefix

        Raises
        ------
            - `TypeError`
                - if arguments have wrong types

        Returns
        -------
            - `rt_mean`
                - `datetime.timedelta`
                - mean runtime over `nreps` function calls
            - `rt_est`
                - `datetime.timedelta`
                - estimated runtime for `nest` function calls

        Dependencies
        ------------
            - `datetime`
            - `numpy`
            - `typing`

        Comments
        --------
    """
    

    #default parameters
    if prefix is None: prefix = ""
    
    #check
    if not isinstance(f, Callable): raise TypeError("`f`, must be of type `Callable`")
    if not isinstance(nreps, int): raise TypeError("`nreps`, must be of type `int`")
    if not isinstance(nest, int): raise TypeError("`nest`, must be of type `int`")
    if not isinstance(prefix, str): raise TypeError("`prefix`, must be of type `str`")

    #do `nreps` repetitions
    durations = []
    for _ in range(nreps):
        start = datetime.now()  #starting time of current execution

        f(*args)    #run function
        end = datetime.now()    #completion time of current execution
        durations.append(end-start)
    
    rt_mean = np.mean(durations)
    rt_est = rt_mean * nest
    logger.info(f"{prefix}mean runtime over {nreps} executions: {rt_mean} => estimate for {nest} executions: {rt_est}")
    return rt_mean, rt_est

def cn5_style():
    """
        - function defining the custom cn5 style

        Parameters
        ----------

        Raises
        ------

        Returs
        ------
            - `hatches`
                - `List[str]`
                - hatches to iterate through for unque hatches
        
        Dependencies
        ------------
            - `cylcler`
            `matplotlib`
        
        Comments
        --------
    """

    hatches = ["/", "\\", "o", "|"]
    prop_cycle = (
        cycler(linestyle=["-","--", ":", "-."]) +
        cycler(color=["#ffffff", "#CA7D33", "#974D13", "#3E2114"])
    )

    #color scheme
    plt.rcParams["figure.facecolor"]        = "#333333"
    plt.rcParams["axes.facecolor"]          = "#333333"
    plt.rcParams["text.color"]              = "#ffffff"
    plt.rcParams["xtick.color"]             = "#ffffff"
    plt.rcParams["ytick.color"]             = "#ffffff"
    plt.rcParams["axes.labelcolor"]         = "#ffffff"
    plt.rcParams["axes.edgecolor"]          = "#ffffff"
    plt.rcParams["legend.facecolor"]        = "inherit"
    plt.rcParams["legend.edgecolor"]        = "inherit"
    plt.rcParams["axes.prop_cycle"]         = prop_cycle
    plt.rcParams["image.cmap"]              = "Oranges"
    plt.rcParams["axes3d.xaxis.panecolor"]  = (1,1,1,.1)
    plt.rcParams["axes3d.yaxis.panecolor"]  = (1,1,1,.1)
    plt.rcParams["axes3d.zaxis.panecolor"]  = (1,1,1,.1)

    return hatches

def plot_lc(ax:plt.Axes,
    time:np.ndarray, flux:np.ndarray, flux_e:np.ndarray, bands:np.ndarray=None,
    unique_bands:Union[List,str]=None, cmap:str="rainbow",
    label:str="",
    ) -> plt.cm.ScalarMappable:
    """
        - function to plot a lightcurve in various passbands with errorbars

        Parameters
        ----------
            - `ax`
                - `plt.Axes`
                - axes to plot into
            - `time`
                - `np.ndarray`
                - times of the measurements
            - `flux`
                - `np.ndarray`
                - fluxes of the measurements
            - `flux_e`
                - `np.ndarray`
                - errors of `flux`
            - `bands`
                - `np.ndarray`, optoinal
                - passbands `flux` got measured in
                - the default is `None`
                    - assumes all measurements have been taken in the same band
            - `unique_bands`
                - `List`, `str`, optional
                - unique bands present in `bands`
                - determines order of plotting
                    - relevant for color assignment
                - the default is `None`
                    - set to `np.unique(bands)`
                - `cmap`
                    - `str`, optional
                    - colormap to use
                    - the default is `rainbow`
                - `label`
                    - `str`, optional
                    - label to assign to the series
                    - the default is `""`
                        - no label

        Raises
        ------

        Returns
        -------
            - `sm`
                - `ScalarMappable`
                - can be used for colorbar creation (`fig.colorbar(sm, cax=...)`)

        Dependencies
        ------------
            - `matplotlib`
            - `numpy`

        Comments
        --------
            - no tests implemented
    """
    
    #default parameters
    if bands is None: bands = np.full_like(time, 0)
    if unique_bands is None: unique_bands = np.unique(bands)
    print(bands, unique_bands)

    #get colors
    norm = mcolors.Normalize(vmin=0, vmax=len(unique_bands))
    cmap = plt.get_cmap(cmap)
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    colors = plt.get_cmap(cmap)(norm(range(len(unique_bands))))

    for (idx, ub) in enumerate(unique_bands):
        mask = (bands == ub)
        ax.errorbar(time[mask],  flux[mask],  yerr=flux_e[mask],  marker=".", ls="", c=colors[idx], label=label*(idx==0))

    return sm

def gen_data(n:int, sigma_nu:float=0.01) -> Tuple[List[np.ndarray],List[float],List[np.ndarray]]:
    """
        - helper function to generate some pseudo data
        - will generate `n` observations for the lc with gaussian noise of level of `sigma_nu`
            - errors are assigned as `2*np.abs(flux_e)`

        Parameters
        ----------
            - `n`
                - `int`
                - number of observations to generate for the lightcurve
            - `sigma_nu`
                - `float`, optional
                - level of (gaussian) noise of the ligthcurve flux measurements
                - the default is `0.01`

        Raises
        ------

        Returns
        -------
            - `images`
                - `List[np.ndarray]`
                - 3 images
                    - im1: random gaussian noise
                    - im2: diagonal gradient
                    - im3: random rgb image
            - `lc_params`
                - `List[float]`
                - parameters used to generate the pseudo lc
                    - `mu1`
                        - mean of first gaussian
                    - `sigma1`
                        - std of first gaussian
                    - `mu2`
                        - mean of second gaussian
                    - `sigma2`
                        - std of second gaussian
            - `lc`
                - `List[np.ndarray]`
                - pseudo measurements of the lc
                    - `measid`
                        - measurment id
                    - `time`
                        - times of the measurment
                    - `flux`
                        - flux at time `time`
                    - `flux_e`
                        - error estimate for `flux`
                    - `band`
                        - passband of the observation

                    
        Depdendencies
        -------------
            - `numpy`

        Comments
        -------- 
            - no tests implemented
    """
    im1 = np.random.randn(10,10)
    im2 = np.arange(50).reshape(5,10)
    im3 = np.random.randint(0, 255, (50, 50, 3), dtype=np.uint8)   #rgb image with random colors    
    images = [im1,im2,im3]

    #get lc
    ##parameters
    unique_bands = list("ugrizy")
    mu1, sigma1 = 40, 20
    mu2, sigma2 = 20, 10 
    lc_params = [mu1, mu2, sigma1, sigma2, unique_bands]
    
    ##measurements
    measid  = np.arange(0,n,1)
    time    = np.linspace(0,1.5*max(mu1, mu2),n) + 0.05*np.random.randn(n)
    flux    = np.exp(-(time - mu1)**2/sigma1**2) + np.exp(-(time - mu2)**2/sigma2**2)
    flux_e  = sigma_nu*np.random.randn(n)         #errorbars and noise
    band    = np.random.choice(unique_bands, size=n)
    lc = [measid,time,flux+flux_e,2*np.abs(flux_e),band]
    
    return images, lc_params, lc

def makefile(filepath:str, force:bool=False):
    """
        - creates a new file
        - if `force==True`: will overwrite any existing file of the same name
        - if `force==False`: will only create a new file if it is not yet existing

        Parameters
        ----------
            - `filepath`
                - `str`
                - path to the file to create
            - `force`
                - `bool`, optional
                - force create the file
                - overwrites existing files with empty file
                - the default is `False`

        Raises
        ------

        Returns
        -------

        Dependencies
        ------------
            - `os`

        Comments
        --------
            - no tests implemented
    """
    
    if not os.path.exists(filepath) or force:   #onlyif `force` or file not yet existent
        open(filepath, "w").close()             #create new, empty file

    return