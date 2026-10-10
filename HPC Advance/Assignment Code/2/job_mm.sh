#!/bin/bash

#SBATCH -J test_job
#SBATCH -N 1
#SBATCH --ntasks-per-node=10
#SBATCH --output=out.txt
#SBATCH --error=error.txt
#SBATCH --partition=hm
#SBATCH --time=00:10:00

export OMP_NUM_THREADS=10

./mm 
