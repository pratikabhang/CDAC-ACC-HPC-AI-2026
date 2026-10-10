#!/bin/bash
#SBATCH --job-name=my_job_array
#SBATCH --output=output_%A_%a.out
#SBATCH --error=error_%A_%a.err
#SBATCH --array=1-2
#SBATCH --nodes=1
#SBATCH --tasks-per-node=4
#SBATCH --time=00:10:00
#SBATCH --partition=standard



# Define an array of parameters
PARAMS=("param1" "param2")

# Get the parameter for the current job array index
MY_PARAM=${PARAMS[$SLURM_ARRAY_TASK_ID-1]}

echo "Running job with parameter: $MY_PARAM"

# Run your program with the parameter
mpirun -np 4 ./mm $MY_PARAM

