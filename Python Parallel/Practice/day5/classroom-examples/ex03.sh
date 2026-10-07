#!/bin/bash

#SBATCH -A tutor
#SBATCH --job-name=ex03
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --time=00:05:00
#SBATCH --output=ex03_%j.out
#SBATCH --error=ex03_%j.err

set -e

# 1. Load compiler and CUDA modules
module purge
module load compiler/gcc/12.3
module load cuda/12.3

# 2. Activate the existing Conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate hpc_env

# 3. Prevent user-site packages from interfering
export PYTHONNOUSERSITE=1

# 4. Run the program
python -u ex03.py
