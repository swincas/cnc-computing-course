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
# [jupyter](https://jupyter.org/) (Notebooks) on OzStar


---

# [IPython](https://ipython.org/)

* interactivity of [jupyter notebooks](#jupyter-notebooks)
* streamlined like standard scripts

```python
#%%cell1 (execute with `shift return`)
a = 1
print(a)
#%%cell2 (execute with `shift return`)
a += 2
print(a)
```