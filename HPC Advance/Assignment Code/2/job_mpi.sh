#!/bin/bash
#SBATCH -J test_job
#SBATCh --nodes=1
#SBATCH --tasks-per-node=4
#SBATCH --partition=standard
#SBATCH --output=mpi_mm.out
#SBATCH --error=error.out
#SBATCH --time=00:10:00

mpirun -np 2 vtune -collect hotspotis ./mpi_mm

