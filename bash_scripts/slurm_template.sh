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
