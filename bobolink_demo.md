Demo of MPI mandelbrot on bobolink
==================================

This code is used for a demo job on our Raspberry pi cluster named
bobolink.
It consists of the mpi-mandelbrot application, a jobscript and a 
viewer.

Compiling
---------

In order to run the application the program has to be compiled first.
It is compiled using compilers installed with EasyBuild.
https://easybuild.readthedocs.io

The GNU compilers and other tools are organized in a toolchain. This
toolchain is called foss/2019a.

To compile the application the module for foss/2019a has to be loaded first, e.g.:

    module load foss/2019a
    make

Without loading the module a different MPI is being used, which is not interfaced
with the SLURM scheduler of the cluster.


Running
-------

To run the application on the compute nodes a job has to be submitted to the scheduler.
An example job is shown in jobscript.sh. The job can be submitted using:

    sbatch jobscript.sh

Viewing the images
------------------

A viewer has been created in Python. This viewer will display the most recent *.bmp image on disk.
After this it will check for new images, and display the latest one.
The viewer can be started using:

    ./showimages.py
