#!/bin/bash

#SBATCH -A tutor
#SBATCH --job-name=ex02
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --time=00:05:00
#SBATCH --output=ex02_%j.out
#SBATCH --error=ex02_%j.err

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

# 4. Print diagnostic information
echo "===== Compiler ====="
which gcc
gcc --version

echo "===== CUDA compiler ====="
which nvcc
nvcc --version

echo "===== Python environment ====="
which python
python --version

echo "===== System header ====="
ls -l /usr/include/features.h || true

echo "===== Node ====="
hostname

# 5. Run the program
python -u ex02.py
