---
tags: bug,enhancement,help-wanted
title: "If you get \"Segmentation fault\", please read!"
html_url: "https://github.com/3fon3fonov/exostriker/issues/60"
user: 3fon3fonov
repo: 3fon3fonov/exostriker
---

Recently, I have noticed that newer versions of PyQt5 on Python3 can crash with "Segmentation fault", without printing the cause of the problem to the stderr/stdout widget of the GUI, or in the main terminal. These are often harmless bugs/problems that were never causing problems on Python2, or an older PyQT5. I am looking for a more general fix for this problem.

If you experience "Segmentation fault", please start the GUI with:

` $python3 exostriker_gui.py -debug`

And try to reproduce the problem. When the GUI crashes, you will see the actual error on the terminal. Then open a new issue with:

* brief description of the problem
* your OS
* your python version 
* your dependencies versions (the "-debug" flag will print this for you) 
* and the log of the error

