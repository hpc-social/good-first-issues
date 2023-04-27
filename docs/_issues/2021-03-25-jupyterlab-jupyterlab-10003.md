---
title: "Audit selectKernel dialog to make sure it always has translator"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/10003"
user: JessicaBarh
repo: jupyterlab/jupyterlab
---

<!--
Welcome! Before creating a new issue:
* Search for relevant issues
* Follow the issue reporting guidelines:
https://jupyterlab.readthedocs.io/en/latest/getting_started/issue.html
-->

## Description
"Select Kernel" dialog does not display in selected UI language. 
the options.translator seems to be null in: https://github.com/jupyterlab/jupyterlab/blob/dd73fa37ef5a4daed6a900ee729cab53f84c7141/packages/apputils/src/sessioncontext.tsx#L320
<!--Describe the bug clearly and concisely. Include screenshots if possible-->
![image](https://user-images.githubusercontent.com/71149531/112410000-da73e480-8cf0-11eb-814f-40c18160d658.png)

![image](https://user-images.githubusercontent.com/71149531/112409831-91bc2b80-8cf0-11eb-8078-00cdb1d5441f.png)

## Reproduce

<!--Describe step-by-step instructions to reproduce the behavior-->

1. Go to File -> New -> Notebook
2. "Select Kernel" dialog comes up


<!--Describe how you diagnosed the issue. See the guidelines at
 https://jupyterlab.readthedocs.io/en/latest/getting_started/issue.html -->

## Expected behavior

![image](https://user-images.githubusercontent.com/71149531/112410991-8669ff80-8cf2-11eb-80e6-a17dec539f10.png)

This is the dialog displayed working correctly if opened by clicking on the kernel name at the top right corner of a notebook:
![image](https://user-images.githubusercontent.com/71149531/112411253-fb3d3980-8cf2-11eb-843f-7cbd9b6327b9.png)

## Context

<!--Complete the following for context, and add any other relevant context-->

- JupyterLab version: 3.0.11


