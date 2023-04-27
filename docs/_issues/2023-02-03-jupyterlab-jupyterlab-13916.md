---
tags: enhancement,help-wanted
title: "Add button closing dangling kernels"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/13916"
user: fcollonval
repo: jupyterlab/jupyterlab
---

> The "dangling" kernel is actually a real live kernel session that still exists but had no visibility before.

It was visible before too (and is on 3.x and 2.x). This is the where users refer to when they run low on memory (killing old kernels from closed notebooks that were previously closed). Maybe we even should have a button for "Kill all kernels which do not have any notebook/console".

On this use-case we could have something like this:

![Screenshot from 2023-01-24 19-53-59](https://user-images.githubusercontent.com/5832902/214395002-c1fbba37-d280-49d3-a28d-d233cd922843.png)

> Note: the numbers in circles on the graphic are irrelevant; those were from an exploration suggesting how to show the number of documents/widgets connected to the kernel.

_Originally posted by @krassowski in https://github.com/jupyterlab/jupyterlab/issues/13779#issuecomment-1402523525_
