#!/bin/bash
#SBATCH --nodes=7
#SBATCH --tasks-per-node=4
#SBATCH --time=08:00:00

module purge
module load foss/2019a

# Interesting coordinates
# Coordinates obtained using: http://math.hws.edu/eck/js/mandelbrot/MB.html
xc=(-0.489025673694519663075 -1.7864403919251484 -1.0100771887517512706077 -0.1627713416)
yc=( 0.607042700155268608770  0.0000000000000000  0.3125869794970174930924 -1.0315908160)

while [ 1 ]; do
    for i in $(seq 0 $(( ${#xc[*]} - 1)) ); do
        echo "Running Mandelbrot for " ${xc[$i]} ", " ${yc[$i]}
        mpirun ./mandelbrot -a 2.0 -x ${xc[$i]}  -y ${yc[$i]} -z 100 -f 0.8 -n 20000
        sleep 10
    done
done
