#!/bin/bash
#SBATCH --partition=dgx
##SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=12:00:00
#SBATCH --gres=gpu:1

#module load gcc
#module load openmpi/1.8.3_gcc-11.3
#module load cp2k/2023.1_ompi-4.1.4

#module load cuda

dvc repro

