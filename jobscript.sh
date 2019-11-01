#!/bin/bash
#SBATCH --nodes=7
#SBATCH --tasks-per-node=4
#SBATCH --time=08:00:00

module purge
module load foss/2019a

# Interesting coordinates
xc=(-0.995246804477361527265  0.3750001200618655 -1.0100771887517512706077 -0.1627713416)
yc=( 0.294453898173439620240 -0.2166393884377127  0.3125869794970174930924 -1.0315908160)


#xc=0.3750001200618655
#yc=-0.2166393884377127

#xc=-0.13856524454488
#yc=-0.64935990748190

#xc=-1.0100771887517512706077
#yc=0.3125869794970174930924

#xc=-0.1627713416
#yc=-1.0315908160


while [ 1 ]; do
    for i in $(seq 0 $(( ${#xc[*]} - 1)) ); do
        echo "Running Mandelbrot for " ${xc[$i]} ", " ${yc[$i]}
        mpirun ./mandelbrot -a 2.0 -x ${xc[$i]}  -y ${yc[$i]} -z 100 -f 0.8 -n 20000
    done
done
