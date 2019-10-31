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

xc=-1.0100771887517512706077
yc=0.3125869794970174930924

xc=-0.1627713416
yc=-1.0315908160

mpirun ./mandelbrot -a 2.0 -x $xc  -y $yc -z 100 -f 0.8 -n 10000

