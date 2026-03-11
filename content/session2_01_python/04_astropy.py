#%%imports
from astropy.coordinates import SkyCoord
from astropy.cosmology import FlatLambdaCDM
from astropy.nddata import Cutout2D
from astropy import units as u
from astropy.wcs import WCS
import logging
import matplotlib.pyplot as plt
import numpy as np
import warnings

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
warnings.filterwarnings("ignore", category=RuntimeWarning)

from cn5_pkg import cn5
hatches = cn5.cn5_style()


#%%definitions
def get_wcs():
    """
        - defines custom WCS
    """
    wcs = WCS(naxis=2)
    wcs.wcs.crpix = [100, 100]                          #reference pixel (center)
    wcs.wcs.cdelt = np.array([-0.000277, 0.000277])     #pixel scale (deg/pix)
    wcs.wcs.crval = [150.0, 2.0]                        #reference coordinates (RA, Dec)
    wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]            #projection type 
    return wcs

def coords():
    """
        - demo for `SkyCoords()`
    """
    ncoords = 10000
    coords1 = SkyCoord(ra="2h30m00s", dec=-45, unit=(u.deg,u.deg), frame="icrs")
    coord_cat = SkyCoord(ra=np.random.randint(0,180,ncoords), dec=np.random.randint(-90,90,ncoords), unit=(u.deg,u.deg), frame="icrs")  #catalog of coords


    #separation
    logger.info(f"separations: {coords1.separation(coord_cat)}")
    
    #crossmatch
    idx, d2d, d3d = coords1.match_to_catalog_3d(coord_cat, nthneighbor=1)
    logger.info(f"closest sources at index {idx} (2d distance: {d2d}, 3d distance: {d3d})")

    return

def cosmology():
    cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
    logger.info(f"h = {cosmo.h}")
    logger.info(f"absmag(m=23.5,z=0.7) = {23.5*u.mag - cosmo.distmod(0.7):.1f}")
    return

def cout2d():
    """
        - demo for `2DCutout()`
    """
    #get wcs
    wcs = get_wcs()

    #define image based on custom wcs
    xpix, ypix = int(2*wcs.wcs.crpix[0]), int(2*wcs.wcs.crpix[1])
    img = np.arange(xpix*ypix).reshape(xpix,ypix)
    
    #perform cutout
    pos = SkyCoord(ra=(wcs.wcs.crval[0]+0.002)*u.deg, dec=(wcs.wcs.crval[1]+0.002)*u.deg, frame="icrs")
    size=(130,30)    #in pixels
    cutout = Cutout2D(img, position=pos, size=size, wcs=wcs)
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection=cutout.wcs, aspect="equal")
    ax2 = fig.add_subplot(122, projection=cutout.wcs, aspect="equal")
    ax2.sharex(ax1)
    ax2.sharey(ax1)
    ax1.set_xlabel("RA")
    ax1.set_ylabel("DEC")
    ax1.set_title("Original")
    ax2.set_title("Cutout")
    im = ax1.pcolormesh(range(0,xpix), range(0,ypix), img, vmin=img.min(), vmax=img.max())
    im = ax2.pcolormesh(range(cutout.xmin_original,cutout.xmax_original+1), range(cutout.ymin_original,cutout.ymax_original+1), cutout.data, vmin=img.min(), vmax=img.max())
    cbar = fig.colorbar(im, cax=fig.add_axes([1.0, 0.31, 0.02, 0.47]))
    cbar.set_label("Flux")
    fig.tight_layout()
    return

#%%main
def main():

    coords()
    cosmology()
    cout2d()

    plt.show()  #avoid multiple `plt.show()`

if __name__ == "__main__":
    main()
