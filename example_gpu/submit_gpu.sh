#!/bin/bash

#SBATCH --job-name=example                   

#SBATCH --account=gpu_gres  # to access gpu resources

#SBATCH --partition=gpu

#SBATCH --nodes=1       # request to run job on single node                                       

#SBATCH --ntasks=5     # request 10 CPU's (t3gpu01: balance between CPU and GPU : 5CPU/1GPU)      

#SBATCH --gres=gpu:1    # request 1 GPU's on machine                                         

python example.py
