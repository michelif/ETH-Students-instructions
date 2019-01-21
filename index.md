## Instructions for students starting with ETH

This page is intended to help arbeit/master students in the first steps of their work with ETH. Send comments to micheli@cern.ch

### 1. Get an account at Tier3

The starting point is to get an account at the T3 @ PSI. You can follow the instructions [here](https://wiki.chipp.ch/twiki/bin/view/CmsTier3/HowToGetAccount). In general, you can specify that you don't
need a GRID account. Ask your supervisor what to put in "physics group", the suggested login shell is /bin/bash.

Basic instructions on how to login and perform basic operations can be found [here](https://wiki.chipp.ch/twiki/bin/view/CmsTier3/HowToSetupYourAccount). Please note that for ETH the user interface host name is t3ui02.psi.ch. 

### 2. Preliminary steps

The first step is to setup the environement for running ROOT and jupyter. [This page](https://wiki.chipp.ch/twiki/bin/view/CmsTier3/HowToWorkInCmsEnv#The_ROOT_Environment_and_Jupyter) collects the needed informations. 
After that try to start a jupyter notebook on a t3 machine

{% highlight python %} 

jupyter notebook --port 8883 --no-browser 

{% endhighlight %}

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

6- It is suggested to get [this php file]() and overwrite the one you got from git. This php allows a better management for plot display

7- change mdonega —>you_username index.php
   (it’s the line    $script_path = "/~mdonega/plots”;   )
   
8- send a mail to isg@phys.ethz.ch and ask them to enable php in your directory adding your supervisor in cc (say it’s the same configuration they made for mdonega) 

9- if everything works you should get something like this: 
     people.phys.ethz.ch/~mdonega/plots/uglyPlots_v9/


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
