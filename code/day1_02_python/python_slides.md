---
marp: true
theme: cn5_style
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