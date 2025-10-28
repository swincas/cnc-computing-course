---
marp: false
theme: cn5_style
footer: slides by Lukas Steinwender
---

<!-- _class: titleslide -->
# Combine
## End2End Workflows

![bg](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---

# Disclaimer

> You don't have to copy someone elses workflow.
> It is most important that you find some workflow that works for you and stick with it to the best of your abilities!
---

# Lukas

## Initial Setup
* create new git repo
    * based on my [RepoTemplate](https://github.com/TheRedElement/RepoTemplate_LuSt/tree/main/code)
* clone created repo to local machine
```bash
git clone --recurse-submodules <repo url>
```

* navigate to code snippets submodule (within created repo) and sync
```bash
cd <path/to/codesnippets>
git pull
```

* navigate to repo and init [mise](../session3_03_uv_mise/01_uv_mise.md) project
```bash
cd <path/to/project>
mise use <version to be used>
```

* if [Python](../session1_02_python/01_python_slides.md)
    * load [uv](../session3_03_uv_mise/01_uv_mise.md)
    * init uv project
```bash
mise use uv@latest
uv init --bare
```

* fill `./README.md` with basic information
* choose a [git](../session1_01_git_github/01_git_github_slides.md) workflow
    * create respective branches
    * **stick with it for the duration of the project**
* start coding

## While Coding
* temporary files and figures have the `temp_` prefix
    * will not be synced to [git](../session1_01_git_github/)
* all created figures are stored in `./report/gfx/`
    * one place for all of them
* progress is reported in `./summary.md`
    * essentially a first draft for the final release/paper
    * includes 
        * [mermaid](https://mermaid.js.org/) flowcharts,
        * figures
        * tables
        * derivations
        * references
            * added to `./report/bib-refs.bib`
        * etc.
* as soon as I use a code-block more than 2 times, it gets refractored into a `function`
* if several `functions` are used in the same context more than 2 times, they get refractored into a `class`
* any constants, `functions` etc. that get used across several files are added to `_projectbuildingblocks.py`
* scripts of the main routine follow a dedicated naming convention
    * see `README.md` in [RepoTemplate](https://github.com/TheRedElement/RepoTemplate_LuSt/tree/main/code)

## Documenting
* any created `function` or `class` gets at least a one-sentence docstring
* once the function/class is moved to a module
    * docstring gets completed

## Writing the Paper
* clone my $\LaTeX$ template (or the journals template) into `./report/`
* start writing
    * all references, equations, figures, etc. should be present through documentation of `./summary.md`

> I only add my paper here, if the repo is not public yet.
> Once the package/report/paper is published, that's when I add the source in `./report/`.