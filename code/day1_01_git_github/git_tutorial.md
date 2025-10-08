---
marp: true
theme: cn5_style
---

<!-- _class: titleslide -->
# Day 1

![bg left:80](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---

# [Git](https://git-scm.com/)
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->
![bg vertical 50% right:20%](../../gfx/logo_git.png)
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->
![bg vertical 50% right:20%](../../gfx/logo_github.png)
![bg vertical 50% right:20%]("")    <!-- placeholder for placment -->

* **local**
* version control
    * editing code without affecting latest working version
* crucial for collaborating on code
* useful for personal projects
* [learn/try interactively](https://learngitbranching.js.org/)


# [GitHub](https://github.com/)
* **remote (cloud)**
* allows to share code with others
<!-- * let's look at a [remote repo](https://github.com/TheRedElement/LuStCodeSnippets/tree/main) -->
* let's look at a [remote repo](https://github.com/swincas/cnc-computing-course.git)

---
# Useful Commands

```bash
#getting the repo
git clone <url/to/repo>
git fork <url/to/repo>
```

```bash
#version update
git status
git pull                        #remote
git diff
git add <yourfiles>
git commit -m "<your message>"
git push                        #remote
git remote [-rm <file>]         #remote interaction                                             
```

```bash
#branching
git checkout [-b] <branchname>
git branch [-a]
git merge <branch to be merged into current branch>
git rebase <branch to be rebased onto current branch>
git log --graph --oneline --decorate --all --color                                      
```

---

## Rebase vs Merge

### Merge
* in principle automatic (requires user action for merge conflicts)

<div class="mermaid">
gitGraph
    commit id: "A"
    commit id: "B"
    branch feature
    checkout feature
        commit id: "C"
    checkout main
    commit id: "D"
    commit id: "E"
    merge feature id: "C "
    commit id: "F"
</div>

### Rebase
<div class="mermaid">
gitGraph
    commit id: "A"
    commit id: "B"
    branch feature
    checkout feature
        commit id: "C"
        commit id: "D"
        commit id: "E"
    checkout main
    cherry-pick id: "C"
    commit id: "D "
    commit id: "E "
</div>


---
## Clone vs Fork

### Clone (Copy Linked to Original)
* sets original repository as origin
* you can sync changes to your local copy if the devs updated the code
* `push` changes will be reflected in the original (if you have permission)

### Fork (New, Isolated Copy)
* completely new copy of repo
    * you are in control of that copy
* original developers do not know about forked copy
* `push` changes only affect your forked copy
* edits to original can be suggested via pull requests

---

# Industry Workflows

## Release-Dev-Feature
<div class="mermaid">
gitGraph
    commit id: "v0.1"
    branch dev
    checkout dev
        branch featureA
        checkout featureA
            commit id: "devA1"
            commit id: "devA2"
        checkout dev
        merge featureA id: "v0.2"
    checkout main
    merge dev id: "v1.0"
    checkout dev
    commit id: "v1.1"
        branch featureB
        checkout featureB
        commit id: "devB1"
        commit id: "devB2"
        commit id: "devB3"
    checkout dev
    merge featureB id: "v1.2"
    checkout main
    merge dev id: "v2.0"
    %% rebase featureB
</div>

---

## Release-Version-Feature
<div class="mermaid">
gitGraph
    commit id: "v0.1"
    branch version1.0
    checkout version1.0
        branch featureA
        checkout featureA
            commit id: "devA1"
            commit id: "devA2"
        checkout version1.0
        merge featureA id: "v0.2"
    checkout main
    merge version1.0 id: "v1.0"
    branch version2.0
    checkout version2.0
        commit id: "v1.1" 
        branch featureB
        checkout featureB
            commit id: "devB1"
            commit id: "devB2"
            commit id: "devB3"
        checkout version2.0
        merge featureB id: "v1.2"
    checkout main
    merge version2.0 id: "v2.0"
</div>


---
# Submodules
* linking to other git-repos
* repo-within a repo
    * changes synced upon `git pull`

```bash
#linking
git submodule add <url/to/git repo>
```

```bash
#unlinking
git config -f .gitmodules --remove-section submodule.path/to/submodule #remvove submodule entry
git config -f .git/config --remove-section submodule.path/to/submodule #remove submodule from git config
git rm --cached path/to/submodule #remove submodule from git's tracking
rm -rf path/to/submodule/.git #delete .git directory (convert to normal directory)

#track changes
git add path/to/submodule
git commit -m "Convert submodule to regular directory"
```

---
# [VSCode](https://code.visualstudio.com/)
* suite of tools for git-incorporation
    * [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
    * `Source Control` (shipped by default)
    * [VSCode](https://code.visualstudio.com/) settings sync
        * through login with [GitHub](https://github.com/) account

---
# Action!

> 1. clone the repo used in this course:
> [https://github.com/swincas/cnc-computing-course.git](https://github.com/swincas/cnc-computing-course.git)

> 2. on [GitHub](http://github.com/), init a new repo that can host all your useful code-snippets
> 3. based on one of the [industry workflows](#industry-workflows), create a `dev` branch that will host your developments detached from `main`
> 4. modify the `README.md` file and push the changes