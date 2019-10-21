#!/bin/bash
#SBATCH --nodes=2
#SBATCH --tasks-per-node=1
##SBATCH --mem=1M
#SBATCH --time=00:30:00

module purge
module load foss/2018a

srun ./mandelbrot -a 1.0 -x -0.835 -y 0.20001 -z 100 -f 0.51
