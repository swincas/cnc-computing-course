# cnc-computing-course
Content for the CAS Cookies-n-Code Computing Course (CN5)
* yes, the slides are pretty full... this is because this repo shall (alongside course material) mainly serve as a resource to find useful information

## TODO
- [ ] [session3_02_interactive_computing/](./content/session3_02_interactive_computing/)
    - [ ] jupyter on ozstar

## Notes

### Installable Parts

> [!IMPORTANT]
> the [cn5_pkg](./cn5_pkg/) is installable.
> This way you can use the utility functions easily in your own scripts.

* the [cn5_pkg](./cn5_pkg/) package contains functions used across diferent sessions in the cn5 course

* To install simply call the following from within your virtual environment:
```bash
pip3 install git+https://github.com/swincas/cnc-computing-course.git
```
* You can then use the function as usual:
```python
from cn5_pkg import cn5
cn5.runtime_estimate(<args>)
```

> [!IMPORTANT]
> If you find the [cn5_pkg](./cn5_pkg/) package useful for your work, a brief acknowledgement would be appreciated:
> We/I acknowledge the Cookie Monsters from the Swinburne Centre for Astrophysics and Supercomping (CAS), who made their utility functions available on github (https://github.com/swincas/cnc-computing-course.git).

### For Cookie Monsters (Presenters)
* to use the custom [cn5_style.css](./styles/cn5_style.css) in the [marpit](https://marpit.marp.app/) slides proceed as follows
    1. open project in [VSCode](https://code.visualstudio.com/)
    2. add [Marp for VSCode](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) addon
    3. open workspace settings
    4. search for `marp theme`
    5. under `Markdown › Marp: Themes` add the following path `styles/cn5_style.css`
* when presenting it is useful to enable `screencast mode`
    * enable via `ctrl+shift+P > Developer: Toggle Screencast Mode`
    * ensures people can see your keystrokes

## Preliminary Tasks For Attendees
- [ ] create git account
- [ ] get OzStar account
- [ ] become member of OzStar project
- [ ] install [git](https://git-scm.com/)
    - Linux (Ubuntu): `apt-get install git`
    - Mac: `brew install git`
    - Windows: download from [here](https://git-scm.com/downloads/win)
- [ ] clone the Cn5 repo
```bash
git clone https://github.com/swincas/cnc-computing-course.git
```

## Agenda
1. Day 1
    1. [git and github](./content/session1_01_git_github/)
    1. [python and venvs](./content/session1_02_python/)
    1. [data formats](./content/session1_03_data_formats/)
1. Day 2
    1. [bash intro](./content/session2_01_bash/)
    1. [hpc and ozstar](./content/session2_02_hpc_ozstar/)
1. Day 3
    1. [uv and mise](./content/session3_01_uv_mise/)
    1. [interactive computing](./content/session3_02_interactive_computing/)
    1. [good practises](./content/session3_03_good_practises/)
1. Day 4
    1. OzSTAR tour
1. Day 5
    1. [vscode](./content/session4_01_vscode/)
    1. [end2end workflows](./content/session4_02_end2end_workflows/)
    1. [ssh keys](./content/session4_03_sshkeys/)
    1. Q&A

## Repo Structure
* [cn5_pkg/](./cn5_pkg/)
    * installable package
    * contains function used throughout the course that might also be useful in your research
* [content/](./content)
    * course material
* [data/](./data/)
    * contains data used and generated throughout the course
* [gfx/](./gfx/)
    * graphics used in presentations and generated when running scripts
* [styles/](./styles/)
    * custom Cn5 styles
        * css style for the slides
        * mplstyle for plots
* [templates/](./templates/)
    * templates to copy and paste
    * i.e., for slides
* [legacy/](./legacy/)
    * contains layouts of previous versions of Cn5
* [.python-version](./.python-version)
    * python version used for development
    * used by [uv](https://docs.astral.sh/uv/)
* [cn5_cheatsheet](./cn5_cheatsheet.pdf)
    * cheat sheet of useful commands
* [mise.toml](./mise.toml)
    * version control of programs used in the project
    * specific to [mise-en-place](https://mise.jdx.dev/)
* [pyproject.toml](./pyproject.toml)
    * file specifying the project
    * necessary for installation of [cn5_pkg/](./cn5_pkg/)
    * contains
        * dependencies
        * version
        * authors
* [requirements_mpi.txt](./requirements_mpi.txt)
    * repirements for installation of packages used throughout the course
    * includes `mpi4pi`
    * compiled from [pyproject.toml](./pyproject.toml)
    * install via `pip3 install -r requirements_mpi.txt`
* [requirements.txt](./requirements.txt)
    * repirements for installation of packages used throughout the course
    * excludes `mpi4pi`
    * compiled from [pyproject.toml](./pyproject.toml)
    * install via `pip3 install -r requirements.txt`
* [uv.lock](./uv.lock)
    * current state of the python environment as observed by [uv](https://docs.astral.sh/uv/)