#!/bin/bash
#SBATCH --time     7-10:01:00
#SBATCH -n 100
#SBATCH --partition xfel-sim
#SBATCH --job-name csrtrack
#SBATCH --output slurm.out
source /etc/profile.d/modules.sh
module load mpi/openmpi-x86_64-intel
date
mpirun /usr/bin/time -p /home/meykopff/bin/csrtrack_intel_openmpi_1.205
date
exit
