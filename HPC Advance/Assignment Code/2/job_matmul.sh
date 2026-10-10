#!/bin/bash
#BATCH -J TestJob
#SBATCH -N 1                      
#SBATCH --ntasks-per-node=2       
#SBATCH --output=3mm.out            
#SBATCH --error=3mm.err              
#SBATCH --partition=standard         
#SBATCH --time=0:02:00              

mpirun -np 2 ./mpi_mm 



