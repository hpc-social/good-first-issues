---
title: "For all Windows users, please read!!! "
html_url: "https://github.com/3fon3fonov/exostriker/issues/106"
user: 3fon3fonov
repo: 3fon3fonov/exostriker
---

I decided to post the installation sequence on Windows 10 & Windows 11 here.
As of June 13, 2022 it goes like this:

1.  ################################  WSL & WSL2  ######################################

Installation on Windows 10 and 11 works only troughs the "Windows Subsystem for Linux".
Please follow this guide:
 
`https://docs.microsoft.com/en-us/windows/wsl/install
`

Follow all the steps carefully! This way you will be able to run all Linux native programs on your WINDOWS 10 & 11
bash shell, which is very useful in general!

Please install the Ubuntu 20.04 LTS !!!

2.  ################################  XServer on your Windows  ############################### 

To make The Exo-Striker work, however, you also will need an XServer installed.
Follow these instructions carefully:

`https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/
`

3.  ################################  Update the kernel  ############################### 

Let's assume you have  installed the Ubuntu 20.04 LTS app on your Windows OS. Now open the app and update the Linux kernel

```
$ sudo apt update 
$ sudo apt dist-upgrade -y 
```

When done, install the following lines:

`$ sudo apt install build-essential curl git gfortran gcc+ csh xterm
`

4.  ################################  Fix the Qt libraries  ############################### 

For some unknown reason, some qt binaries in Ubuntu 20.04+ are missing. Just in case, run all these commands:

```
$ sudo apt install libxcb-xinerama0
$ sudo apt install libxkbcommon-x11-0
$ sudo apt install qt5-default
```

5.  ################################  Install Python3.8  and pip3.8 ###############################
 
Python3.8+ is strongly recommended!!! On your WSL on Windows and Ubuntu 20.04, you will likely have python3.8.2 installed, but to install the newest python3.8.13 alongside your system python3.8.2 you can try these instructions (for 18.04 but should be OK for 20.04): 

`https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/
`

Let's assume, you have python3.8, then it is recommended to install pip3.8:

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3.8 get-pip.py
```

6.  ################################  Install python-dev ###############################

For yet another unknown reason, a fresh Ubuntu 20.04 does not include the Python Development files. 

`$ sudo apt install python3-dev
`

7.  ################################  Install the Exo-Striker  ###############################

At this point, your system should be clean of all problems preventing the Exo-Striker being installed. Keep in mind, your python3.8 system is likely quite "empty". To install all the dependencies in one-go, the recommended way is:
 
`$ pip3.8 install git+https://github.com/3fon3fonov/exostriker --user
`
/for user installation -- recommended !!!!!!/

Then just run:

`$ exostriker`

If the GUI looks like this:
 
![bad_screen](https://user-images.githubusercontent.com/44244057/173373799-dc9b5f70-2bf5-4500-85db-077fe0820e83.png)


Then your  Screen scaling is probably 150%. Go to "Change the resolution of the display" and reduce it to 100% and the GUI will look fine like this:

![good_screen](https://user-images.githubusercontent.com/44244057/173373950-3cad0014-5dc1-4a10-9653-2b93bf32a983.png)


I hope this not-so-short guide helped!


################################ Bonus tip ###############################

 I generally recommend to work with git clone / git pull to always get the new version: E.g., 


```
$ cd ~
$ git clone https://github.com/3fon3fonov/exostriker
$ cd exostriker
$ python3.8 exostriker_gui.py 
```

The latter command will open the GUI inside the root "exostriker" directory and will be easy to find your sessions and files. One can even rename the directory:

 
`$ mv exostriker exostriker_GL486 
`
or 
```
$ cp -r  exostriker exostriker_GL486
$ cp -r  exostriker exostriker_GL876
$ cp -r  exostriker exostriker_GL1148
```
etc.,

I.e., your analysis of GL486 will be stored in ~/exostriker_GL486. To work and/or update the repo:

```
$ cd exostriker_GL486 
$ git pull 
$ python3.8 exostriker_gui.py 
```
 
If problems occur:

`$ python3.8 exostriker_gui.py -debug 
`

,and open an issue here.


