# cnc-computing-course
Content for the CAS Cookies-n-Code Computing Course (CN5)


## Notes For Presentors
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
    - Linuc (Ubuntu): `apt-get install git`
    - Mac: `brew install git`
    - Windows: download from [here](https://git-scm.com/downloads/win)
- [ ] clone the Cn5 repo
```bash
git clone https://github.com/swincas/cnc-computing-course.git -b main CnC
```


## Agenda
1. VSCode intro
1. git and github
    1. init CodeSnippets repo
1. python
    1. venvs
    1. astropy
        1. fits
        1. units
    1. matplotlib + styles
    1. pandas (polars)
    1. logging vs print
    1. unit tests
1. Bash
    * history
    * reverse search
    * symlinks
1. OzStar + HPC
    1. ssh
    1. quota + filesystems, storage
    1. I/O
    1. modules
    1. .bashrc
    1. screen
    1. slurm
    1. script profiling
    1. types of parallelism
        1. job arrays (exist if needed)
    1. gpu
1. uv + mise
1. interactive computing
    1. jupyter
    1. ipython
    1. google colab
    1. homebrew
1. VScode
    1. LaTeX in VScode
    1. debugger
    1. extension
1. example end2end workflows
    1. Obsidian
1. Q&A
1. sshkeys (optional)

## Repo Structure
* [code/](./src)
    * contains examples and tasks for the course
* [legacy/](./legacy/)
    * contains layouts of previous versions of Cn5
* [mise.toml](./mise.toml)
    * version control of programs used in the project
    * specific to [mise-en-place](https://mise.jdx.dev/)
* [pyproject.toml](./pyproject.toml)
    * file specifying the project
    * contains
        * dependencies
        * version
        * authors
* [requirements.txt](./reqirements.txt)
    * requirements file for the convenience of pip users
    * compiled from [pyproject.toml](./pyproject.toml)
* [uv.lock](./uv.lock)
    * current state of the python environment as observed by [UV](https://docs.astral.sh/uv/)