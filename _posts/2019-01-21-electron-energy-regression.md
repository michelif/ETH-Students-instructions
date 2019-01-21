This page collects the instructions for the basic setup of electron energy regresion with Neural Networks.

### First get the code:

Fork to your directory the code here: https://github.com/michelif/HHbbgg_ETH 
Clone it locally:

```bash
git clone git@github.com:[YOURNAME]/HHbbgg_ETH.git HHbbgg_ETH_devel 
```
You should create your own branch, then do pull requests when you are done. 


### Prepare the environment 

```bash
ssh -L 8889:localhost:8889  mdonega@t3ui02.psi.ch
screen 
ssh -L 8889:localhost:8889  mdonega@t3gpu01
source bootJupyter.sh
```

Set the ROOT Environment and Jupyter/IPython and check that your env variables are correct

```bash
Which python:
```
should give /scratch/musella/anaconda3/bin/python

```bash
Which anaconda:
```

should give /scratch/musella/anaconda3/bin/anaconda

```bash
conda env list
```
should give:

```bash
base                  *  /scratch/musella/anaconda3
cern_root                /scratch/musella/anaconda3/envs/cern_root
hub                      /scratch/musella/anaconda3/envs/hub
pytorch                  /scratch/musella/anaconda3/envs/pytorch
tensorflow               /scratch/musella/anaconda3/envs/tensorflow
```

Activate tensorflow with:

```bash
source activate tensorflow
```

Remember to set your scratch env variable

```bash
export SCRATCH=/scratch/mdonega/
```

### Run the training:

Check which GPU is free… (in the example below they are all free i.e 0% in the first table - ignore the second table -)
(tensorflow) 

```bash
nvidia-smi
```

You should get an output like 

```bash
Thu Nov  1 17:09:01 2018
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 390.30                 Driver Version: 390.30                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  Off  | 00000000:04:00.0 Off |                  N/A |
| 25%   31C    P0    57W / 250W |      0MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 108...  Off  | 00000000:06:00.0 Off |                  N/A |
| 25%   29C    P0    56W / 250W |      0MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   2  GeForce GTX 108...  Off  | 00000000:07:00.0 Off |                  N/A |
| 25%   30C    P0    58W / 250W |      0MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   3  GeForce GTX 108...  Off  | 00000000:08:00.0 Off |                  N/A |
| 25%   28C    P0    56W / 250W |      0MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   4  GeForce GTX 108...  Off  | 00000000:0C:00.0 Off |                  N/A |
| 25%   29C    P0    58W / 250W |      0MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   5  GeForce GTX 108...  Off  | 00000000:0D:00.0 Off |                  N/A |
| 25%   31C    P0    58W / 250W |      0MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   6  GeForce GTX 108...  Off  | 00000000:0E:00.0 Off |                  N/A |
| 25%   29C    P0    57W / 250W |      0MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   7  GeForce GTX 108...  Off  | 00000000:0F:00.0 Off |                  N/A |
| 25%   27C    P0    57W / 250W |      0MiB / 11178MiB |      2%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

In the commands below the string CUDA_VISIBLE_DEVICES=1 is used to select the GPU:
Choose a reasonable number of epochs

```bash
CUDA_VISIBLE_DEVICES=1 python train_ffwd_phoEnergy.py --inp-dir=/scratch/mdonega/ntuples_NN --inp-file=Ntup_10Nov_Photon_training_allvars.hd5 --out-dir test --loss mse --epochs=1
```

To Apply the training:
```bash
CUDA_VISIBLE_DEVICES=1 ipython -i predict_fit_ffwd_phoEnergy.py -- --training mse --inp-dir=/scratch/mdonega/ntuples_NN/ --inp-file=Ntup_10Nov_Photon_training_allvars.hd5 --target-dir=./test --out-dir=./files_PhotonRegNN_applied
```

To plot the results:
```bash
jupyter notebook —port 8889 —no-browser
```

select the kernel —> ```Python [conda env:tensorflow] ```
and run the  ```/GPU/HHbbgg_ETH_devel/bregression/notebooks/plot_phoEnergy.ipynb```
  -> modifying the path to the dir/file of the results:
	inp_dir='./'
	inp_file='files_PhotonRegNN_appliedapplied_res_2018-11-01_Ntup_10Nov_Photon_training_allvars.hd5'

