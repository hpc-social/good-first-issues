---
tags: enhancement,pkgfilebrowser,tagFeature-Parity
title: "For notebook v7: tree view should be able to sort notebook ahead of other files."
html_url: "https://github.com/jupyterlab/jupyterlab/issues/14332"
user: Carreau
repo: jupyterlab/jupyterlab
---

See upstream issue https://github.com/jupyter/notebook/issues/6819

### Problem

Notebook V6 tree view sorts `folders > notebook > other files`, reason being in notebook users are way less likely to access other files. 

As V7 uses JupyterLab Components notebook get sorted as they are in JupyterLab, and thus we lost having notebooks at the top of the tree view. 

### Proposed Solution

Add an option for the file browser to sort notebooks preferentially. Folder are already on top, so it should not be too hard. 
