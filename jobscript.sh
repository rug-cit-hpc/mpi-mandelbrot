#!/bin/bash
#SBATCH --nodes=7
#SBATCH --tasks-per-node=4
#SBATCH --time=00:30:00

module purge
module load foss/2019a

# Interesting coordinates
xc=-0.995246804477361527265
yc=0.294453898173439620240

#xc=0.3750001200618655
#yc=-0.2166393884377127

#xc=-0.13856524454488
#yc=-0.64935990748190

mpirun -n 5 ./mandelbrot -a 2.0 -x $xc  -y $yc -z 100 -f 0.8 -n 10000

