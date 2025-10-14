---
marp: true
theme: cn5_style
footer: slides created Lukas Steinwender
---

<!-- _class: titleslide -->
# Control 
## Python and <br> Virtual Environments <br> Packages

![bg](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---

# [Python](https://www.python.org/)

![bg 30% vertical right:30%](../../gfx/logo_python.png)
![bg 30% vertical right:30%]("")
![bg 30% vertical right:30%]("")
![bg 30% vertical right:30%]("")

> exeuctable pseudo code

* high-level + multi-purpose
* readability > speed
* object oriented language (OOL)
* very popular
    * many resources exist
    * community developed packages and modules

## two-language problem
* prototyping in slow language
* deployment needs translation to fast language

---

# Virtual Environments

> every project deserves its own environment

* isolate project from operating system
    * prevents breaks when installing packages somewhere else
* can easily be done with [venv](#venv) package


---
# [venv](https://docs.python.org/3/library/venv.html)

```bash
python -m venv <name/your/env>                      #creation
source <path/to/env>/bin/activate                   #activation
```
```bash
python -m pip install <name of package>             #installation
pip install <name of package>                       #installation
pip install -r <path/to/requirements.txt>           #installation
pip list                                            #listing
```
```bash
pip freeze > <path/to/requirements.txt>             #sharing
```

> choose your own package manager (I recommend pip).
> Whatever you do, try **NOT** to mix package manager (i.e., conda + pip)

---
# Action!

> in your copy of [https://github.com/swincas/cnc-computing-course.git](https://github.com/swincas/cnc-computing-course.git)
> 1. initialize a new [virtual environment](#virtual-environments)
> 1. activate it
> 1. install all the packages needed for the remainder of the course using the [requirements.txt](../../reqirements.txt) file

<!--
in code-snippets git repo use UV (later in the course)
-->

---
# Good To Know
* you can install your own packages (if they are configured accordingly)
    * need a `setup.py` or `pyproject.toml`
* `-e` installs the file in editable mode
    * any changes you make to the source will be reflected in the installed version

```bash
pip3 install -e <path/to/your/package> 
```

* keep your venv clean with [pipreqs](https://github.com/bndr/pipreqs)
    * creates [requirements.txt](../../reqirements.txt) that only contains packages that get used in your project
        * ignores depdencies of these packages

```bash
    pip3 install pipreqs    #install
    pipreqs . --force       #create (force to overwrite existing file)
```

---
# Useful Packages
---

# [NumPy](https://numpy.org/)

![bg 50% vertical right:30%](../../gfx/logo_numpy.png)
![bg 50% vertical right:30%]("")
![bg 50% vertical right:30%]("")
![bg 50% vertical right:30%]("")

* main package for numerical computations
* philosophy
    * vectorization > parallelisation
* row-indexed
* need for speed
    * compile to `C`
    * consistent data types
    * views > copies
* enhancements: `np.einsum()`, [Einops](https://einops.rocks/)

> make use of `@np.vecrtorize` to increase speed ([example](../day2_02_hpc_ozstar/02_parallel_computing.py))

---

![bg 100% vertical right:50%](../../gfx/loto_matplotlib.png)
![bg 100% vertical right:50%]("")

# [Matplotlib](https://matplotlib.org/)
* [Python's](https://www.python.org/) plotting library
* highly customizable

render-hieararchy:
1. Canvas
1. Containers: Figure, Axes
1. Artist: lines, markers, text, ...

---
## Design Guidelines
* understandable without extra explanation
    * caption should guide the user, not substitute the plot
* readable
    * font-size
    * clutter
* understandable without colours
* should present key result

> most paper readers look at the plots **before** reading the text.
> the plot shall sell your result/idea

---
## Customizing [Matplotlib](https://matplotlib.org/)
### Approach 1: [style sheets](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-style-sheets)
* default [matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#matplotlibrc-sample)
* use via the following

```python
plt.style.use("<path/to/yout/file.mplstyle")
```

### Approach 2: Function + `plt.rcParams`
* see [this repo](https://github.com/TheRedElement/LuStCodeSnippets/blob/main/LuStCodeSnippets_py/Styles/PlotStyles.py) for examples
* see [here](https://github.com/TheRedElement/LuStCodeSnippets/blob/main/LuStCodeSnippets_py_demos/Styles_demos/PlotStyles_demo.ipynb) for usage demos

---
# Data Frames
![bg 50% vertical right:30%]("")
![bg 50% vertical right:30%](../../gfx/logo_pandas.svg)
![bg 50% vertical right:30%]("")
![bg 50% vertical right:30%](../../gfx/logo_polars.png)
![bg 50% vertical right:30%]("")

## [pandas](https://pandas.pydata.org/)
* processing tabular data efficiently
* loads of convenience methods and functions
* has some convenient plotting capabilities

## [Polars](https://pola.rs/)
* [Pandas](#pandas) on steroids
* not as many conveniences, but but efficient in
    * memory
    * speed

---
![bg 70% vertical right:30%]("")
![bg 70% vertical right:30%](../../gfx/logo_astropy.png)
![bg 70% vertical right:30%]("")
![bg 70% vertical right:30%]("")

# [Astropy](https://docs.astropy.org/)
* developed specifically for astronomy
* useful intergations
    * astronomical data-formats
    * units
    * coordinates
    * coordinate systems

---
## Snippets
* [ND data processing](https://docs.astropy.org/en/latest/nddata/index.html)
```python
from astropy.nddata import Cutout2D
cutout = Cutout2D(<img>, position=<coords_center>, size=<size_pixels>, wcs=<img_wcs>)                           
fig, axs = plt.subplots(1,1, suplot_kw=dict(projection=cutout.wcs))
axs.imshow(cutoput.data)
```
* [coordinates](https://docs.astropy.org/en/stable/coordinates/index.html)
```python
from astropy.coordinates import SkyCoord
coords1 = SkyCoord(ra=<ra>, dec=<dec>, unit=(<ra_unit>,<dec_unit>), frame="fk5")
coords2 = SkyCoord(ra=<ra>, dec=<dec>, unit=(<ra_unit>,<dec_unit>), frame="fk5")                
idx, d2d, d3d = coords2.mathr_co_catalog_3d(coords1)    #crossmatch
dists = coords1.separation(coords2)                     #separation
```
* [FlatLambdaCDM](https://docs.astropy.org/en/stable/api/astropy.cosmology.LambdaCDM.html) cosmology
```python
from astropy.cosmology import LambdaCDM                                                     
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
```
---

# Other Useful Packages
* [Scipy](https://scipy.org/)
    * variety of tools useful in scientific computing
    * see stats-course by *Chris Blake*
* [joblib](https://joblib.readthedocs.io/)
    * see [later session](../day2_02_hpc_ozstar/)
* [mpi4py](https://mpi4py.readthedocs.io/)
    * see [later session](../day2_02_hpc_ozstar/)
* [seaborn](https://seaborn.pydata.org/)
    * statistical data visualization
* [scikit-learn](https://scikit-learn.org/)
    * (shallow) machine learning in [Python](https://www.python.org/)

---
# Good Practises: [Logging](https://docs.python.org/3/library/logging.html)
* `print()` can go haywire especially on supercomputer
* [Logging](https://docs.python.org/3/library/logging.html) allows customization of displayed messages

```python
import logging
logger = logging.getLogger()                    #root logger
local_logger = logging.getLogger(__name__)      #local logger
logging.basicConfig(level=logging.WARNING)      #only show warnings
local_logger.setLevel(logging.DEBUG)            #all logged messages

logger.info("hidden")
logger.warning("shown")
local_logger.info("not hidden")
local_logger.warning("shown")
```

---
# Good Practises: Unit Tests
* unit tests ensure that your code does not break
* crucial for collaboration

> investing 30 min to write a good test prevents hours of headache down the line

* useful module: [pytest](https://docs.pytest.org/)

```python
#content of test_sample.py
def inc(x):
    return x + 1
def test_answer():
    assert inc(3) == 5
```
```bash
pytest <path/to/test/directory>
```
