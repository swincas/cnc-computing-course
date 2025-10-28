---
marp: true
theme: cn5_style
footer: slides by Lukas Steinwender
---

<!-- _class: titleslide -->
# Contain
## mise-en-place and uv

![bg](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---

# [mise-en-place](https://mise.jdx.dev/) (mise)

* development environment setup tool
    * tool version manager
    * allows switching between set of environment variables
    * can manage and run tasks
* installs via [mise](https://mise.jdx.dev/) can be much faster than installing from scratch
* creates isolated environments for each project and knows which versions, environments, etc. to use

> [mise](https://mise.jdx.dev/) does most of the things you should do for you

<br>

$$\textcolor{red}{\text{\large unfortunately NOT useable on OzStar (quota limit)}}$$

---

## Global Setup

* [installation](https://mise.jdx.dev/getting-started.html)
```bash
curl https://mise.run | sh
~/.local/bin/mise --version                                     #testing
echo "" >> ~/.bashrc                                            #add to .bashrc
echo "#%%activate mise-en-place" >> ~/.bashrc                   #add to .bashrc
echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc   #add to .bashrc                         
```

* global installs
```bash
mise use --global python@latest   #latest version of Python                                 
mise use --global uv@latest       #uv python manager
```

* inspect
```bash
mise list               #installed tools
mise ls-remote <tool>   #all available versions of tool
```

---
## Setting Up a Project
* follow along in your code-snippets git repo
* navigate to your project root
* get utilities

```bash
mise use python@<version>
mise use uv@<version>
```
* set environment variables
```bash
mise set MY_VAR=123
```

---
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->
![bg vertical 50% right:20%](../../gfx/logo_uv.png)
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->

# [uv](https://docs.astral.sh/uv/)

> every projects deserves its own virtual environemnt

* efficient python project manager
    * environments
    * packages
* written in [rust](https://rust-lang.org/)
    * much faster than [poetry](https://python-poetry.org/), [pip](https://pypi.org/project/pip/), [conda](https://anaconda.org/anaconda/conda), etc.

> [uv](https://docs.astral.sh/uv/) does most of the things you should do for you

<br>

$$\textcolor{red}{\text{\large unfortunately NOT useable on OzStar (quota limit)}}$$
$$\textcolor{green}{\text{\large but there's a workaround ;)}}$$

---
## Workflow
* init project
```bash
uv init <project-name>
uv init <project-name> --bare    #minimal project
```
* add packages
```bash
uv add <package-name>[>=version] [--dev] [--group] [--optional]
uv add git+<https-link>
```
* remove packages
```bash
uv remove <package-name>
```
---
## Integration with [venv](./../session1_02_python/01_python_slides.md)
```bash
uv pip compile pyproject.toml -o requirements.txt 
python3 -m venv .venv
source .venv
pip3 install -r requirements.txt
```

## Comandline Tools
* powerful for code that is executed often
> use a separate uv project for each commandline tool

```bash
uv init --package <package-name>
uv run <command>
```
* see [commandlinetool/](../session3_01_good_practises/commandlinetool/) for an example
---
# End2End Workflow
```bash
#create project
mkdir testproject
cd testproject
#add relevant software
mise use python@3.11
mise use uv@latest
#init project
uv init --package .
#run from commandline
uv run testproject
```