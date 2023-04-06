---
tags: ,bug,tagCSS
title: "Wrong mouse cursor when hovering a kernel in the Running tab"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/14326"
user: jtpio
repo: jupyterlab/jupyterlab
---

<!-- Welcome! Thank you for contributing. These HTML comments will not render in the issue.

Before creating a new issue:
* Search for relevant issues
* Follow the issue reporting guidelines:
https://jupyterlab.readthedocs.io/en/latest/getting_started/issue.html
-->

## Description

Hovering on kernel entries in the `Running`tab shows a "wrong" mouse cursor

<!--Describe the bug clearly and concisely. Include screenshots if possible-->

## Reproduce

<!--Describe step-by-step instructions to reproduce the behavior-->

1. Open JupyterLab 4.0.0b0
2. Create a notebook
3. Open the Running tab
4. Hover on the kernels

https://user-images.githubusercontent.com/591645/229863722-a48cb99a-d2e1-4ffd-99ae-f21581f63afb.mp4

## Expected behavior

The mouse cursor should not be a text insertion-point `cursor`.

## Context

JupyterLab `4.0.0b0` on Firefox 111.
