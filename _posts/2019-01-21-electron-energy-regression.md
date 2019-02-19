This page collects the instructions for the basic setup of electron energy regresion with Neural Networks.
The basic instructions and prerequisites to run GPUs at Tier3 can be found here <https://michelif.github.io/ETH-Students-instructions/2019/01/21/instructions.html>

### First get the code:

Fork to your directory the code here: https://github.com/michelif/HHbbgg_ETH 
Clone it locally:

```bash
git clone git@github.com:[YOURNAME]/HHbbgg_ETH.git HHbbgg_ETH_devel 
```
You should create your own branch, then do pull requests when you are done. 


### Prepare the environment 

```bash
ssh -L 8889:localhost:8889  [USERNAME]@t3ui02.psi.ch
screen 
# only the first time you login get this configuration script
cp /t3home/mdonega/bootJupyter.sh .
ssh -L 8889:localhost:8889  [USERNAME]@t3login
source ./bootJupyter.sh
```
The t3login is only a virtual machine used to submit jobs to the GPUs

Running bootJupyter.sh you should get

```bash
SET THE ROOT Environment and Jupyter/IPython
Which python:
/shome/mdonega/anaconda3/bin/python
Which anaconda:
/shome/mdonega/anaconda3/bin/anaconda
```

You can check the installed conda environments by:

```bash
conda env list
```
should give:

```bash
# conda environments:
#
base                  *  /shome/mdonega/anaconda3
cern_root                /shome/mdonega/anaconda3/envs/cern_root
pytorch                  /shome/mdonega/anaconda3/envs/pytorch
tensorflow               /shome/mdonega/anaconda3/envs/tensorflow
tensorflow_gpu           /shome/mdonega/anaconda3/envs/tensorflow_gpu
xgboost                  /shome/mdonega/anaconda3/envs/xgboost
```

Activate tensorflow with:

```bash
source activate tensorflow_gpu
```
you should see:

```bash
(tensorflow_gpu) mdonega@t3ui02:~ >
```

(and deactivate when you are done)
```bash
source deactivate
```
Remember to set your scratch env variable

```bash
export SCRATCH=/scratch/[USERNAME]
```

### Submit jobs to the GPUs:

Prepare a script myJob.sh e.g.:
```
#!/bin/bash
#SBATCH --job-name=test_gpu
#SBATCH --account=test  # to access gpu resources
#SBATCH --nodes=1       # request to run job on single node
#SBATCH --ntasks=10     # request 10 CPU's (t3gpu01: balance between CPU and GPU : 5CPU/1GPU)
#SBATCH --gres=gpu:1    # request 2 GPU's on machine
#SBATCH --time=00:08:00 # time limit of job (8 minutes)
#SBATCH --partition=gpu

echo HOSTNAME
hostname
echo CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES

python [my python training script]
```

as an example [my python training script] could be "train_ffwd_phoEnergy.py --inp-dir=./tmp/ --inp-file=Ntup_10Nov_Photon_training_allvars.hd5 --out-dir ./tmp/ --loss mse --epochs=1"

To submit the job
> sbatch myJob.sh

### Some useful commands to control your jobs:

SLURM is used as scheduler for the GPU.
(google for slurm commands if you need more)

Submit jobs:
```bash
sbatch myJob.sh
```

Cheeck your jobs:
```bash
squeue -u <username>
```

Status of your jobs:
```bash
sstat --format=AveCPU,AvePages,AveRSS,AveVMSize,JobID -j <jobid> --allsteps
```

Kill jobs:
```bash
scancel <jobid>
```

