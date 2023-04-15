---
tags: documentation,help-wanted
title: "Missing Node.js error message unclear"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/8459"
user: big-o
repo: jupyterlab/jupyterlab
---

<!--
Welcome! Before creating a new issue:
* Search for relevant issues
* Follow the issue reporting guidelines:
https://jupyterlab.readthedocs.io/en/latest/getting_started/issue.html
-->

## Description

I've just made the move over from Jupyter Notebook to JupyterLab. Really impressed so far, but I had one issue that took me a little while to debug, and I believe a more clear error message would have resolved this for me straight away.

## Reproduce

<!--Describe step-by-step instructions to reproduce the behavior-->

Try installing an extension on a machine without nodejs/npm installed and you'll get an error message saying "please install Node.js". However, a simple `sudo apt install nodejs` is not enough. You also need to install `npm`. With node and no npm, JupyterLab still fails to install the extension and you don't get an error message.

<!--Describe how you diagnosed the issue. See the guidelines at
 https://jupyterlab.readthedocs.io/en/latest/getting_started/issue.html -->

## Expected behavior

<!--Describe what you expected to happen-->

Amend the error message to say `Please install Node.js AND npm`.

## Context

<!--Complete the following for context, and add any other relevant context-->

- Operating System and version: Ubuntu 20.04
- Browser and version: Chromium 81
- JupyterLab version: 2.1.2