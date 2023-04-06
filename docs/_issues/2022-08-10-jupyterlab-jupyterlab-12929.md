---
tags: ,enhancement,pkgfilebrowser
title: "Open/limit FileDialog.getExistingDirectory from a subdir of root"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/12929"
user: suganya-sk
repo: jupyterlab/jupyterlab
---

### Problem
The current `FileDialog.getExistingDirectory` is great for getting user input as a directory. While this is very useful, it opens, by default, from the root dir of the app. 

I could not find an option to modify this in the docs - https://jupyterlab.readthedocs.io/en/stable/api/interfaces/filebrowser.filedialog.idirectoryoptions.html

### Proposed Solution

* Add an option to accept the path of the subdir from which `FileDialog.getExistingDirectory` should open.
* This could also mean that it must not be possible to navigate to a dir higher than the path provided, in this dialog.