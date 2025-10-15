#Lukas Steinwender

#%%imports
from astropy.io import fits
from astropy.table import Table
import h5py
from IPython.display import display
import logging
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import os
import pandas as pd
import sys
from typing import List, Tuple, Union

DIR_PATH:str = os.path.dirname(os.path.realpath(__file__)) + "/"    #path to current directory
ROOT_PATH:str = f"{DIR_PATH}../../"                                 #path to project root
sys.path.append(ROOT_PATH)                                          #make sure root is visible to python

from cn5_pkg import cn5

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


#%%definitions
def gen_data(n:int, sigma_nu:float=0.01) -> Tuple[List[np.ndarray],List[float],List[np.ndarray]]:
    """
        - helper function to generate data
        - will generate `n` observations for the lc with gaussian noise of level of `sigma_nu`
            - errors are assigned as `2*np.abs(flux_e)`
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

def plot_lc(ax:plt.Axes,
    time, flux, flux_e, bands,
    unique_bands, cmap:str="rainbow",
    label="",
    ) -> plt.cm.ScalarMappable:
    """
        - helper function to plot a lightcurve in various passbands with errorbars
    """
    
    #get colors
    norm = mcolors.Normalize(vmin=0, vmax=len(unique_bands))
    cmap = plt.get_cmap(cmap)
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    colors = plt.get_cmap(cmap)(norm(range(len(unique_bands))))

    for (idx, ub) in enumerate(unique_bands):
        mask = (bands == ub)
        ax.errorbar(time[mask],  flux[mask],  yerr=flux_e[mask],  marker=".", ls="", c=colors[idx], label=label*(idx==0))

    return sm

def makefits(datadir:str):
    """
        - function to create two fits files
            - one from scratch
            - one from a table
    """

    #get data
    images, lc_params, lc = gen_data(100, 0.01)
    im1, im2, im3 = images
    mu1, mu2, sigma1, sigma2, unique_bands = lc_params
    measid, time, flux, flux_e, band = lc 
    
    #######################
    #creation from scratch#
    #######################
    #primary hdu
    hdu0 = fits.PrimaryHDU(data=im1, header=None)
    hdu0.header["OBJECT"]   = "Example Image"
    hdu0.header["AUTHOR"]   = "Cn5"
    hdu0.header["COMMENT"]  = "Gaussian Noise"
    
    #image hdu (extension)
    hdu1 = fits.ImageHDU(data=im2, name="ANOTHER_IMAGE")
    
    #bintable hdu (extension)
    ##save lc
    col0 = fits.Column("id", array=time, format="I")                    #int
    col1 = fits.Column("time", array=time, format="E")                  #float
    col2 = fits.Column("flux", array=flux+flux_e, format="E")           #float
    col3 = fits.Column("flux_e", array=2*np.abs(flux_e), format="E")      #float
    col4 = fits.Column("band", array=band, format="A1")                 #one character string
    hdu2 = fits.BinTableHDU.from_columns([col0,col1,col2,col3,col4], name="BINTABLE")
    hdu2.header["BANDS"] = "".join(unique_bands)
    hdu2.header["DESCRIPT"] = "random lc constructed from two gaussians"

    #ascii table hdu (extension)
    col1 = fits.Column(name="parameter", array=["mu1", "mu2", "sigma1", "sigma2"], format="A10")    #10 character string
    col2 = fits.Column(name="value", array=[mu1, mu2, sigma1, sigma2], format="E")                  #float
    hdu3 = fits.TableHDU.from_columns([col1, col2], name="ASCIITABLE")
    hdu3.header["DESCRIPT"] = "parameters of the lc"

    #compressed image hdu (extension)
    hdu4 = fits.CompImageHDU(data=im3, name='COMPRESSED')
    hdu4.header["DESCRIPT"] = "compressed rgb image with random colors"

    #combine and save
    hdul = fits.HDUList([hdu0, hdu1, hdu2, hdu3, hdu4])
    hdul.writeto(datadir+"fitsdemo_complete.fits", overwrite=True)
    
    ############
    #from table#
    ############
    images, lc_params, lc = gen_data(30, 0.05)

    tab = Table(data=lc, names=["id","time","flux","flux_e","band"])
    tab.write(datadir+"fitsdemo_table.fits", format="fits", overwrite=True)
    return

def loadfits(datadir:str):
    """
        - function to load the created fits files and visualize the content
    """
    
    with fits.open(datadir+"fitsdemo_complete.fits") as hdul:
        logger.info(hdul.info())
        # for hdu in hdul: logger.info(hdu.header)    #in scripts
        for hdu in hdul: display(hdu.header)        #has a nice display in IPython

        #get data
        im1 = hdul[0].data
        im2 = hdul[1].data
        im3 = hdul[-1].data
    
    #plot images (data acessible outside of `with ... as ...:`)
    fig, axs = plt.subplots(1,3, sharex=False, sharey=False, subplot_kw=dict(xlabel="Pixel", ylabel="Pixel"))
    axs[0].imshow(im1)
    axs[1].imshow(im2)
    axs[2].imshow(im3)
    fig.tight_layout()

    #reading in main loop
    hdul = fits.open(datadir+"fitsdemo_complete.fits")
    lc = hdul[2].data
    lc_params = hdul[3].data
    unq_bands = list(hdul[2].header["BANDS"])       #unique bands stored in header
    hdul.close()        #NOTE: DON'T FORGET TO CLOSE!!! 

    #reading directly from table
    tab = Table.read(datadir+"fitsdemo_table.fits", format="fits")

    #plotting lc
    fig, axs = plt.subplots(1,2, sharex=True, sharey=True, subplot_kw=dict(xlabel="Time", ylabel="Flux"))
    fig.suptitle(", ".join([f"{k}={v}" for (k,v) in zip(lc_params["parameter"],lc_params["value"])]))
    sm = plot_lc(axs[0], lc["time"],  lc["flux"],  lc["flux_e"],  lc["band"],  unq_bands, "rainbow", label="FITS")
    sm = plot_lc(axs[1], tab["time"], tab["flux"], tab["flux_e"], tab["band"], unq_bands, "rainbow", label="FITS")

    cax = fig.add_axes([1.0, 0.12, 0.03, 0.78])
    cbar = fig.colorbar(sm, cax=cax)
    cbar.set_ticks(np.linspace(1, len(unq_bands), len(unq_bands))-0.5, labels=unq_bands)
    cbar.set_label("Passband")
    axs[0].legend()
    axs[1].legend()
    fig.tight_layout()

    return

def makeparquet(datadir:str):
    """
        - function to create a parquet file
    """
    #get data
    _, _, lc = gen_data(100, 0.01)

    df = pd.DataFrame(data=dict(
        id=lc[0],
        time=lc[1],
        flux=lc[2],
        flux_e=lc[3],
        band=lc[4],
    ))

    df.to_parquet(datadir+"parquet_demo.parquet", index=False)

    return

def loadparquet(datadir:str):
    """
        - function to load the created parquet file and visualize the content
    """
    df = pd.read_parquet(datadir+"parquet_demo.parquet")
    display(df)
    # logger.info(df)

    #plotting lc
    unq_bands = list("ugrizy")
    fig, axs = plt.subplots(1,1, subplot_kw=dict(xlabel="Time", ylabel="Flux"))
    sm = plot_lc(axs, df["time"],  df["flux"],  df["flux_e"],  df["band"],  unq_bands, "rainbow", label="DataFrame")

    cax = fig.add_axes([1.0, 0.12, 0.03, 0.78])
    cbar = fig.colorbar(sm, cax=cax)
    cbar.set_ticks(np.linspace(1, len(unq_bands), len(unq_bands))-0.5, labels=unq_bands)
    cbar.set_label("Passband")
    axs.legend()
    fig.tight_layout()

    return

def makehdf5(datadir:str):
    """
        - function to create an hdf5 file
    """
    
    #get data
    images, lc_params, lc = gen_data(100, 0.01)
    im1, im2, im3 = images
    mu1, mu2, sigma1, sigma2, unique_bands = lc_params
    measid, time, flux, flux_e, band = lc 
    
    #create file
    f = h5py.File(datadir+"hdf5_demo.h5", "w")
    
    ##group for images
    grp1 = f.create_group("images")
    ds11 = grp1.create_dataset("observation",   data=im1, dtype=float)
    ds12 = grp1.create_dataset("gradient",      data=im2, dtype=float)
    ds13 = grp1.create_dataset("colors",        data=im3, dtype=float)
    ##group for LC
    grp2 = f.create_group("lightcurve")
    ds21 = grp2.create_dataset("measid",        data=measid, dtype=int)
    ds22 = grp2.create_dataset("time",          data=time, dtype=float)
    ds23 = grp2.create_dataset("flux",          data=flux, dtype=float)
    ds24 = grp2.create_dataset("flux_e",        data=flux_e, dtype=float)
    ds25 = grp2.create_dataset("band",          data=band.astype("S1"))     #strings need to be specified explicitly
    ###add metadata
    grp2.attrs["mu1"] = mu1
    grp2.attrs["mu2"] = mu2
    grp2.attrs["sigma1"] = sigma1
    grp2.attrs["sigma2"] = sigma2
    grp2.attrs["unique_bands"] = "".join(unique_bands)

    f.close()

    return

def loadhdf5(datadir:str):
    """
        - function to load the created hdf5 file and visualize the content
    """    

    #read data
    f = h5py.File(datadir+"hdf5_demo.h5", "r")
    im1 = f["images"]["observation"][:]
    im2 = f["images"]["gradient"][:]
    im3 = f["images"]["colors"][:]
    
    time = f["lightcurve"]["time"][:]
    flux = f["lightcurve"]["flux"][:]
    flux_e = f["lightcurve"]["flux_e"][:]
    band = f["lightcurve"]["band"][:].astype(str)
    unq_bands = f["lightcurve"].attrs["unique_bands"]
    lc_params = list(f["lightcurve"].attrs.items())[:-1]
    f.close()

    #plot images
    fig, axs = plt.subplots(1,3, sharex=False, sharey=False, subplot_kw=dict(xlabel="Pixel", ylabel="Pixel"))
    axs[0].imshow(im1)
    axs[1].imshow(im2)
    axs[2].imshow(im3.astype(np.int64))
    fig.tight_layout()

    #plotting lc
    fig, axs = plt.subplots(1,1, sharex=True, sharey=True, subplot_kw=dict(xlabel="Time", ylabel="Flux"))
    fig.suptitle(", ".join([f"{k}={v}" for (k,v) in lc_params]))
    sm = plot_lc(axs, time,  flux,  flux_e,  band,  unq_bands, "rainbow", label="HDF5")

    cax = fig.add_axes([1.0, 0.12, 0.03, 0.78])
    cbar = fig.colorbar(sm, cax=cax)
    cbar.set_ticks(np.linspace(1, len(unq_bands), len(unq_bands))-0.5, labels=unq_bands)
    cbar.set_label("Passband")
    axs.legend()
    fig.tight_layout()

    return
#%%main
def main():
    makefits(f"{ROOT_PATH}data/")
    loadfits(f"{ROOT_PATH}data/")
    makeparquet(f"{ROOT_PATH}data/")
    loadparquet(f"{ROOT_PATH}data/")
    makehdf5(f"{ROOT_PATH}data/")
    loadhdf5(f"{ROOT_PATH}data/")
    return

if __name__ == "__main__":
    main()

    plt.show()  #avoid multiple `plt.show()` in your script
