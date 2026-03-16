#!/bin/bash

#SBATCH --mail-type=NONE #ALL

#SBATCH --job-name=cnc_test_script      #job name

##SBATCH --array=0-2                     #slurm array to execute multiple jobs at once
#SBATCH --output=./execlogs/%x_%a.out
#SBATCH --error=./execlogs/%x_%a.err

#SBATCH --ntasks=1                      #number of tasks per node
#SBATCH --mem=1G                        #total amount of memory per node (in case you are using slurm array)
#SBATCH --time=0-00:20:00               #time limit
##SBATCH --gres=gpu:2                    #request GPUs (amount of GPUs after colon)
##SBATCH --tmp=150GB                     #temporary memory (if large files are acessed, loads of files are read and write)

#load modules

#run your stuff
i=0
while true; do
    echo $i
    sleep 1
    ((i++))
done
