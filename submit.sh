#!/bin/bash
#SBATCH --partition=single
##SBATCH --tasks-per-node=1
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=16gb

module load devel/cuda/11.6

dvc exp run --run-all
