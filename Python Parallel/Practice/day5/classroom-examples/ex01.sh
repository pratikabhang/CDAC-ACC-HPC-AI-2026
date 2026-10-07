#! /bin/bash

#SBATCH -A tutor
#SBATCH --job-name=ex01
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --time=00:05:00
#SBATCH --output=ex01_%j.out
#SBATCH --error=ex01_%j.err

# 1. load the modules
module purge
module load compiler/gcc/12.3
module load cuda/12.3

# 2. activate conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate hpc_env

#3. prevent ~/.local user packages from interfering 
export PYTHONNOUSERSITE=1

python -u ex01.py
