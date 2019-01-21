## Instructions for students starting with ETH

This page is intended to help arbeit/master students in the first steps of their work with ETH. Send comments to micheli@cern.ch

### 1. Get an account at Tier3

The starting point is to get an account at the T3 @ PSI. You can follow the instructions [here](https://wiki.chipp.ch/twiki/bin/view/CmsTier3/HowToGetAccount). In general, you can specify that you don't
need a GRID account. Ask your supervisor what to put in "physics group", the suggested login shell is /bin/bash.

Basic instructions on how to login and perform basic operations can be found [here](https://wiki.chipp.ch/twiki/bin/view/CmsTier3/HowToSetupYourAccount). Please note that for ETH the user interface host name is t3ui02.psi.ch. 

### 2. Preliminary steps

The first step is to setup the environement for running ROOT and jupyter. [This page](https://wiki.chipp.ch/twiki/bin/view/CmsTier3/HowToWorkInCmsEnv#The_ROOT_Environment_and_Jupyter) collects the needed informations. 
After that try to start a jupyter notebook on a t3 machine:

```python
jupyter notebook --port 8883 --no-browser 
```

where 8883 has to be changed with the number of the PORT you used for setup.

Open a local browser on your laptop and go to http://localhost:8883/tree 

### 3. Setting up a web-page

We will need a lot of plots. A convenient way is to look at them is to create a web-page for them.

Instructions:

0- Access your directory on people.phys.etz.ch following https://readme.phys.ethz.ch/storage/access/

1- cut an paste the lines in  "Creating the homepage - Short description for Linux and Mac command line users” from :https://readme.phys.ethz.ch/web/how_to_get_a_personal_homepage/

2- create in public_html a directory called plots.

3- cd plots

4- git clone https://github.com/musella/php-plots.git 

5- follow the instruction in the README in https://github.com/musella/php-plots

6- It is suggested to get [this php file](https://github.com/michelif/ETH-Students-instuctions/blob/master/index_for_students.php) and overwrite the one you got from git. This php allows a better management for plot display

7- change mdonega —>you_username index.php
   (it’s the line    $script_path = "/~mdonega/plots”;   )
   
8- send a mail to isg@phys.ethz.ch and ask them to enable php in your directory adding your supervisor in cc (say it’s the same configuration they made for mdonega) 

9- if everything works you should get something like this: 
     people.phys.ethz.ch/~mdonega/plots/uglyPlots_v9/
     
### How to use GPUs on Tier3

1. Get a Tier3 computing account and make sure that you can log in to the /t3home (use pwd to check if you are in the correct home directory). In case you dont have an account yet or only a shome directory contact the Tier3 admins. The t3home space is limited to 10GB, for bigger files use the shome directory or storage element.

2. Login to the GPUs using:

{% highlight bash %} 
ssh t3gpu01
{% endhighlight %}

3. Set correct environment in order to use python and all libraries needed:

{% highlight bash %} 
export PATH=/scratch/musella/anaconda3/bin:$PATH
{% endhighlight %}

which loads 4 environments which can be shown by using:

{% highlight bash %} 
conda env list
{% endhighlight %}

- base (loads all basic packages with jupyter)
- cern root (ROOT6, not compatible with jupyter, but has root numpy, root pandas) 
- tensorflow (most important environment to train NNs)
- pytorch

Choose correct environment (e.g. for training tensorflow) by running

{% highlight bash %} 
source activate tensorflow
{% endhighlight %}

4. Check which GPUs are in use
{% highlight bash %} 
nvidia−smi
{% endhighlight %}

set the GPU number to one that is not in use by setting the environment variable CUDA VISIBLE DEVICES
before executing the script, e.g. in order to use GPU 1

{% highlight bash %} 
CUDA VISIBLE DEVICES=1 ./ train .py
{% endhighlight %}


in the python script the tensorflow device mapping can be checked by adding:

{% highlight python %} 
import tensorflow as tf
import tensorflow . keras . backend as K

sess = tf.Session(config=tf.ConfigProto(log device placement=True))
K. set session(sess)
{% endhighlight %}

5. after starting the training, open new terminal, login to GPUs again and check GPU usage by running
{% highlight bash %} 
nvidia−smi
{% endhighlight %}

6. in case you have questions or want to join the mattermost channel in which we discuss questions or general stuff
regarding the GPUs, write an email to christina.reissel@cern.ch.

### Useful references

Photons in CMS: https://arxiv.org/abs/1502.02702 
Electrons in CMS: https://arxiv.org/abs/1502.02701
Reconstruction and Identification algorithms, read the section "Photon Reconstruction and Selection” in http://www.roma1.infn.it/cms/tesiPHD/soffi.pdf


### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/michelif/ETH-Students-instuctions/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
