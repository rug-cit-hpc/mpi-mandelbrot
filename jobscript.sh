#!/bin/bash
#SBATCH --nodes=7
#SBATCH --tasks-per-node=4
#SBATCH --time=00:30:00

module purge
module load foss/2019a

srun ./mandelbrot -a 1.0 -x -0.835 -y 0.20001000001 -z 100 -f 0.8 -n 10000
