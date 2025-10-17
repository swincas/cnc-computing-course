---
marp: true
theme: cn5_style
footer: slides by Lukas Steinwender
---

<!-- _class: titleslide -->
# Curiosity
## Interactive Computing

![bg](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---

<!-- in the meantime, colab supports julia as well -->

# [jupyter](https://jupyter.org/) (Notebooks)
* interactive computing
    * [julia](https://julialang.org/)
    * [Python](https://python.org/)
    * [R](https://www.r-project.org/)

> good for exploration, demos, and teaching
> we recommend getting used to scripts

> [Google Colab](https://colab.google/) for quick tests without installs
> also GPU tests possible

* alternative: [IPython](#ipython)

---
# [jupyter](https://jupyter.org/) (Notebooks) on [OzSTAR](../session2_02_hpc_ozstar/01_hpc_ozstar.md)
* *ellegedly* you can use [jupyter](https://jupyter.org/) on [OzSTAR](../session2_02_hpc_ozstar/01_hpc_ozstar.md)
    * these are their [instructions](https://supercomputing.swin.edu.au/docs/2-ozstar/Notebooks.html)
    * I was not able to get it to work in my browser
    * works fine with [VSCode](https://code.visualstudio.com/)
* launching a [jupyter](https://jupyter.org/) server in your browser
```bash
source <path/to/env>/bin/activate
pip3 install jupyter    #install if not installed
jupyter lab --no-browser --port=8888
#copy http://localhost:<portnumber>/tree/token=<token> into your browser
```
 
---
# [IPython](https://ipython.org/)

* interactivity of [jupyter notebooks](#jupyter-notebooks)
* streamlined like standard scripts
* examples: run `find ./content/ -type f -name "*.py"` from project root

```python
#%%cell1 (execute with `shift return`)
a = 1
print(a)
#%%cell2 (execute with `shift return`)
a += 2
print(a)
```