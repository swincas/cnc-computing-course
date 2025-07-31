#!/bin/bash
#
#SBATCH --ntasks=2
#SBATCH --time=10:00
#SBATCH --mem=2GB

srun --ntasks=2 --mem=2GB script.sh
# srun --ntasks=2 script2.sh


# run python array
# srun --ntasks=2 script3.sh
