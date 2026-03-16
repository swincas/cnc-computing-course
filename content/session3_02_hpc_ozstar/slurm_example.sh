#!/bin/bash

#SBATCH --mail-type=NONE #ALL

#SBATCH --job-name=temp_myjob     #job name

#SBATCH --output=./execlogs/%x_%a.out
#SBATCH --error=./execlogs/%x_%a.err

#SBATCH --ntasks=1                      #number of tasks per node
#SBATCH --mem=4G                        #total amount of memory per node (in case you are using slurm array)
#SBATCH --time=0-00:05:00               #time limit

#load modules
# module load python-scientific/3.13.1-foss-2025a #scientific python packages

#run your stuff
# cp /path/to/file.txt $JOBFS               #copy large files to temporary directory
# source .venv/bin/activate                 #activate environment
python3 -c $'
import os
print("Current directory:", os.getcwd())
for i in range(3):
    print(f"Iteration {i}")
'
# deactivate                                #deactivate environment

# cp $JOBFS/path/to/output.txt /path/to/target/directory #don't forget to copy your results back                                      
