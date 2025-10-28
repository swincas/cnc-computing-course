---
marp: true
theme: cn5_style
footer: slides by Lukas Steinwender
---

<!-- _class: titleslide -->
# Compute
## HPC on OzSTAR

![bg](../../gfx/TitlePage.png)
<div class="footnote">Image generated with ChatGPT</div>

---
# Components
<!-- Ngarrgu Tindebeek: "knowledge of the void" in Woiwurrung (provided by Wurundjeri elders) -->
<!-- Tooarrana: endangered Australian animal -->
<!-- Farnakle: Australian slang for "wasting time or engaging in inconsequential activity that creates a false appearance of productivity" -->

<div class="footnote">Source: <a href=https://supercomputing.swin.edu.au/docs>OzSTAR docs</a> (2025/10)</div>

| Unit | OzSTAR (2018) | Ngarrgu Tindebeek (NT, 2023) |
| :-: | :-: | :-: |
| CPU | 4140| 11648 |
| GPU | 230 | 88 |
| OS | AlmaLinux 9 | AlmaLinux 9 |

> the [OzSTAR docs](https://supercomputing.swin.edu.au/docs/) are pretty comprehensive and good
> you might even find some things that are useful outside of HPC

---
# Nodes
<div class="footnote">Source: <a href=https://supercomputing.swin.edu.au/docs>OzSTAR docs</a> (2025-10)</div>

* access points to the HPC

| Node | Type | Application |
| :- | :- | :- |
| farnakle1/farnakle2       | LOGIN nodes (OzSTAR)  | user interaction |
| tooarrana1/tooarrana2     | LOGIN nodes (NT)      | user interaction |
| Farnakle (john, bryan)    | HEAD nodes (OzSTAR)   | compute |
| Tooarrana (dave, gina)    | HEAD nodes (NT)       | compute |
| trevor                    | cloud-compute         | outside communication |
| data-mover                | file transfer         | large file transfers |

---
# SSH: Accessing OzSTAR

* Secure SHell
* protocoll used for connecting to remote hosts
```bash
ssh user@<host>
```
* remember this command?
```bash
quota
```
* in case `quota` are exceeded or you need specific custom software
    * use [Apptainers](https://supercomputing.swin.edu.au/docs/2-ozstar/Apptainer.html)
        * isolate anything contained

---
# Modules
* prepackaged stacks of software
* can be loaded and used
* some modules might depend on others
    * loading order matters!

```bash
module spider [<pattern>]   #list all modules (following <pattern>)
module load <module name>   #load a module
module list                 #show loaded modules
module avail                #list available modules
module purge                #unload all modules                                                 
```

```bash
#relevant modules for Cn5
module purge
module load gcc/12.2.0          #compiler (required for python)
module load python/3.11.2-bare  #minimal installation of python
module load ipython/9.3.0       #for interactive computing
# module load python-scientific/3.13.1-foss-2025a #scientific python packages                    
```

---
# Let's Set Up a [.bashrc](../session1_01_bash/01_bash.md) on OzSTAR!
* adding commonly used modules
* adding aliases


---
# Screen Sessions
* [cheat sheet](https://gist.github.com/jctosta/af918e1618682638aa82)
* running terminal processes in background

```
screen -S <name>    #start new session with name `name`
screen -R <name>    #connect if existing, else create new
screen -r <name>    #connect to existing screen
screen -ls          #list active screen sessions
screen -d <name>    #force detach running session
screen -X -S <name> #force kill a session
```
* keybindings
    * `ctrl+a+d` ... detach from current session
    * `ctrl+d` ... quit current session

> even if you're logged out, your screen keeps running

---
# [SLURM](https://slurm.schedmd.com/documentation.html) (Simple Linux Utility for Resource Management)
<div class="footnote">
By Unknown author - Own work; traced from PNG images at https://slurm.net/branding/ (EPS files mentioned on this website are unavailable), GPL, https://commons.wikimedia.org/w/index.php?curid=49374769
</div>

![bg 50% vertical right:20%]("")
![bg 50% vertical right:20%](../../gfx/logo_slurm.png)
![bg 50% vertical right:20%]("")
![bg 50% vertical right:20%]("")

* HPC resource manager
* highly customizable (by admins)
* mangages
    * job queue
    * resource assignment
    * [job monitoring](https://supercomputing.swin.edu.au/monitor/)
---
## SLURM Commands
<!-- `sinteractive` allows limited number of cores, limited amount of memory -->

* [cheat sheet](https://supercomputing.swin.edu.au/docs/2-ozstar/oz-slurm-basics.html)

```bash
sbatch <path/to/slurm/script.sh>                                #launch a job
srun <path/to/slurm/script.sh>                                  #launch parallel job
sinfo [-s] [-N] [-l]                                            #get information about cluster components
squeue [-u <username>]                                          #check the queue
scancel [<job_id>] [-u <username>] [-t PD]                      #kill a running job `-t PD`: cancel all pending jobs
sinteractive --time=0:20:00 --mem=16g --cpus-per-task=8 --x11   #launch interactive session
jobreport <job_id>                                              #current resource usage of job
```

### Let's Play on OzSTAR!

---
## Resource Requests
<!-- OzSTAR: if you ask for <4GB memory, job will never get flagged -->
* every job requires knowledge of
    * memory: peak memory consumption
    * time: total time required for execution
    * cores: maximum number of cores required at the same time
    * temporary memory
* [estimating resources](#resource-estimate)
    * memory
        * largest object + buffer
        * tools for estimation: [Memory Profiler](https://github.com/pythonprofilers/memory_profiler)
    * time
        * longest loop + buffer
        * I/O are detremental to time
---
### Resource Estimate

* for memory checkout [Memory Profiler](https://github.com/pythonprofilers/memory_profiler)
* from project root run the following:
```bash
source .venv/bin/activate   #activate environment
mprof run code/session2_02_hpc_ozstar/01_resource_estimate.py
mprof plot -o "mprofile_plot.png"
```
* [01_resource_estimate.py](code/session2_02_hpc_ozstar/01_resource_estimate.py) contains
    * function to estimate resources
    * main function to be executed

---
## SLURM Scripts
* check [this repo](https://github.com/TheRedElement/RepoTemplate_LuSt/blob/main/code/bash/slurm_template.sh) for a more comprehensive template

```bash
#!/bin/bash

#SBATCH --mail-type=NONE #ALL

#SBATCH --job-name=myjob     #job name

#SBATCH --array=0-2                     #slurm array to execute multiple jobs at once
#SBATCH --output=./execlogs/%x_%a.out
#SBATCH --error=./execlogs/%x_%a.err

#SBATCH --ntasks=1                      #number of tasks per node
#SBATCH --mem=4G                        #total amount of memory per node (in case you are using slurm array)
#SBATCH --time=2-00:00:00               #time limit
##SBATCH --gres=gpu:2                    #request GPUs (amount of GPUs after colon)
#SBATCH --tmp=150GB                     #temporary memory (if large files are acessed, loads of files are read and write)

#load modules
module load python-scientific/3.13.1-foss-2025a #scientific python packages

#run your stuff
cp /path/to/file.txt $JOBFS             #copy large files to temporary directory

source ~/<path2env>/bash/bin/activate   #activate environment
python3 <path2file.py>                  #run your files
deactivate                              #deactivate environment

cp $JOBFS/path/to/output.txt /path/to/target/directory #don't forget to copy your results back                                      
```