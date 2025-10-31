#%%imports
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from typing import List
import warnings
warnings.filterwarnings("ignore")   #filter warnings

DIR_PATH:str = os.path.dirname(os.path.realpath(__file__)) + "/"    #path to current directory
ROOT_PATH:str = f"{DIR_PATH}../../"                                 #path to project root
sys.path.append(ROOT_PATH)                                          #make sure root is visible to python

logger = logging.getLogger()
logging.basicConfig(level=logging.WARNING)

from cn5_pkg import cn5


#%%definitions
def testplot(hatches:List[str]=None):
    """
        - testplot to demo different styles
    """
    if hatches is None: hatches = [None] * 4

    x = np.linspace(-1,1,10)
    p = np.arange(0,5,1)
    xx, yy = np.meshgrid(x, x)
    zz = xx**2 + yy**3

    fig, axs = plt.subplots(2,2)
    for pi in p:
        axs[0,0].scatter(x, x**pi, label=f"x^{pi}")
        axs[0,0].plot(x, x**pi, label=f"x^{pi}")

    axs[0,1].pcolormesh(xx, yy, zz)

    fig.delaxes(axs[1,0])  # remove the old axes
    ax3d = fig.add_subplot(223, projection="3d")
    ax3d.plot_surface(xx, yy, zz, cmap="Oranges")

    axs[1,1].hist(np.random.randn(1000), hatch=hatches[0])
    axs[1,1].hist(np.random.randn(1000)-1, hatch=hatches[1])

    axs = fig.axes
    for ax in axs:
        ax.legend(ncol=2)
        ax.set_xlabel("x")
        ax.set_ylabel("y")

    fig.tight_layout()

    return



#%%main
def main():
    #default style
    testplot()

    #using style sheet
    plt.style.use(f"{ROOT_PATH}styles/cn5.mplstyle")
    testplot()
    plt.style.use("default")    #back to default

    #using function with `plt.rcParams`
    hatches = cn5.cn5_style()
    # plt.savefig("temp.png")
    testplot(hatches)

    #in-place modifications
    plt.rcParams["figure.facecolor"] = "#DE0000"
    plt.rcParams["savefig.transparent"] = True
    testplot(hatches)
    
    plt.style.use("default")    #back to default

    plt.show()  #avoid multiple `plt.show()`


if __name__ == "__main__":
    main()