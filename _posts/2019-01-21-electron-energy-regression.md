This page collects the instructions for the basic setup of electron energy regresion with Neural Networks.

### First get the code:

Fork to your directory the code here: https://github.com/michelif/HHbbgg_ETH 
Clone it locally:

```
git clone git@github.com:[YOURNAME]/HHbbgg_ETH.git HHbbgg_ETH_devel 
You should create your own branch, then do pull requests when you are done. 
```

Prepare the environment to run the regression:

[mauro@macmd4:~ >ssh -L 8889:localhost:8889  mdonega@t3ui02.psi.ch

[mdonega@t3ui02:~ >screen 

[mdonega@t3ui02:~ >ssh -L 8889:localhost:8889  mdonega@t3gpu01

[mdonega@t3gpu01:~ >source bootJupyter.sh
SET THE ROOT Environment and Jupyter/IPython
Which python:
/scratch/musella/anaconda3/bin/python
Which anaconda:
/scratch/musella/anaconda3/bin/anaconda

xcheck the environments
mdonega@t3gpu01:~ >conda env list
# conda environments:
#
base                  *  /scratch/musella/anaconda3
cern_root                /scratch/musella/anaconda3/envs/cern_root
hub                      /scratch/musella/anaconda3/envs/hub
pytorch                  /scratch/musella/anaconda3/envs/pytorch
tensorflow               /scratch/musella/anaconda3/envs/tensorflow

[mdonega@t3gpu01:~ >source activate tensorflow
(tensorflow) [mdonega@t3gpu01:~ >

Remember to set your scratch env variable
export SCRATCH=/scratch/mdonega/

To Run the training:

Check which GPU is free… (in the example below they are all free i.e 0% in the first table - ignore the second table -)
(tensorflow) [mdonega@t3gpu01:~/GPU/HHbbgg_ETH_devel/bregression/notebooks >nvidia-smi
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

In the commands below the string CUDA_VISIBLE_DEVICES=1 is used to select the GPU:
Choose a reasonable number of epochs

(tensorflow) [mdonega@t3gpu01:~/GPU/HHbbgg_ETH_devel/bregression/notebooks > CUDA_VISIBLE_DEVICES=1 python train_ffwd_phoEnergy.py --inp-dir=/scratch/mdonega/ntuples_NN --inp-file=Ntup_10Nov_Photon_training_allvars.hd5 --out-dir test --loss mse --epochs=1

To Apply the training:

(tensorflow) [mdonega@t3gpu01:~/GPU/HHbbgg_ETH_devel/bregression/notebooks >CUDA_VISIBLE_DEVICES=1 ipython -i predict_fit_ffwd_phoEnergy.py -- --training mse --inp-dir=/scratch/mdonega/ntuples_NN/ --inp-file=Ntup_10Nov_Photon_training_allvars.hd5 --target-dir=./test --out-dir=./files_PhotonRegNN_applied

To plot the results:
(tensorflow) [mdonega@t3gpu01:~/GPU/HHbbgg_ETH_devel/bregression/notebooks >jupyter notebook —port 8889 —no-browser
select the kernel —> Python [conda env:tensorflow] 
and run the  /GPU/HHbbgg_ETH_devel/bregression/notebooks/plot_phoEnergy.ipynb 
  -> modifying the path to the dir/file of the results 
	inp_dir='./'
	inp_file='files_PhotonRegNN_appliedapplied_res_2018-11-01_Ntup_10Nov_Photon_training_allvars.hd5'

