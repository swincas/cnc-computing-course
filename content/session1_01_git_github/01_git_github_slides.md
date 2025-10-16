---
marp: true
theme: cn5_style
footer: slides by Lukas Steinwender
---

<!-- _class: titleslide -->
# Control 
## Git and Github

![bg](../../gfx/TitlePage.png)
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

```mermaid
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
```

### Rebase
```mermaid
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
```


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
* edits to original can be suggested via [pull requests](#pull-requests)

---
## Pull Requests
* [fork](#fork-new-isolated-copy) repository you want to contribute to
* `git clone` [forked repo](#fork-new-isolated-copy) to your local machine
* create new working branch: `git checkout -b <your feature>`
* make changes
* `add`, `commit`, `push`
* on [GitHub](#github)
    * navigate to `pull request` tab
    * click `new pull request`
    * select you want to merge from on the right (your new branch)
    * select branch to merge into on the left (main of original repo)
    * click `create pull request`

---
# Industry Workflows
---

## GitHub Flow

```mermaid
gitGraph
    commit id: "initial commit"
    branch feature1
    checkout feature1
        commit id: "change1"
    checkout main
    merge feature1 id: "v1.0"
    branch feature2
    checkout feature2
        commit id: "change2.1"
    checkout main
    branch feature3
    checkout feature3
        commit id: "change3"
    checkout feature2
    commit id: "change2.2"
    checkout main
    merge feature2 id: "v2.0"
    merge feature3 id: "v3.0"
```
* lightweight
* small projects
* straightforward
* continuous integration
* fast feedback

---

## Git Flow
```mermaid
    gitGraph
        commit id: "v0.1"
        %%setup long-lived branches
        branch hotfix order: 2
        branch dev order: 3
        %%add commit history
        checkout dev
            commit id: "new feature1"
        checkout hotfix
            commit id: "fix1"
        checkout main
            merge hotfix id: "v0.2"
        checkout dev
            branch feature1 order: 5
        checkout feature1
            commit id: "feature1.1"
        checkout dev
            commit id: "new feature2"
            branch feature2 order: 4
        checkout feature2
            commit id: "feature2.1"
        checkout dev
            merge hotfix
        checkout feature2
            commit id: "feature2.2"
        checkout feature1
            commit id: "feature1.2"
        checkout dev
            merge feature2
        branch release order: 2
        checkout release
            commit id: "release testing"
            commit id: "release bug fixes"
        checkout main
            merge release id: "v1.0"
        checkout dev
            merge release
        checkout feature1
            commit id: "feature1.3"
```

* more complex
* allows parallel development
* main branch remains stable


---

## Dev-Feature (Simplification of [Git Flow](#git-flow))

```mermaid
gitGraph
    commit id: "v0.1"
    branch hotfix
    branch dev
    checkout hotfix
        commit id: "hf1"
        commit id: "hf2"
    checkout main
    merge hotfix id: "v0.2"
    checkout dev
        branch featureA
        checkout featureA
            commit id: "devA1"
            commit id: "devA2"
        checkout dev
        merge featureA id: "dev1.0"
    checkout main
    merge dev id: "v1.0"
    checkout main
    checkout dev
    commit id: "dev2.0"
        branch featureB
        checkout featureB
        commit id: "devB1"
        commit id: "devB2"
        commit id: "devB3"
    checkout dev
    merge featureB id: "dev2.01"
    checkout main
    merge dev id: "v2.0"
```

* my simplification of [Git Flow](#git-flow)
* stable main branch
* no parallel development of features
* dev for nightly builds

---
## Version-Feature

```mermaid
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
```

* my enhancement on [GitHub Flow](#github-flow)
* stable main branch
* version branches
        * keep history
        * nightly builds
* feature branches for each version
* no parallel development of features


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

---
# Good To Know

## [GitHub Education](https://github.com/education/students)
* requires picture of student card
* benefits
    * free [GitHub pro](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) account
    * [GitHub Copilot](https://github.com/features/copilot)
    * unlimited repos
    * cloud coding space
    * loads of courses
