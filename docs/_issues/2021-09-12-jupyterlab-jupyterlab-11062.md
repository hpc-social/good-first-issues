---
tags: bug
title: "Don't render incorrectly formatted inline math/latex as math text"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/11062"
user: joelostblom
repo: jupyterlab/jupyterlab
---

## Description

[Pandoc/nbconvert does not allow any spaces immediately after the first or before the last `$`](https://github.com/jupyter/nbconvert/issues/1172#issuecomment-576323320), So instead of typing e.g.  `$ \mu = 3 $` you need to type `$\mu = 3$`. However, JupyterLab renders both of these as math text, and you will only discover that something is wrong when trying to export to latex PDF. Since it looks correctly rendered in the notebook it is particularly difficult to identify the cause of the PDF export failing. This is also the reason for https://github.com/jupyterlab/jupyterlab/issues/8046.

## Reproduce

Create a new notebook with `$ \mu = 3 $` in a markdown cell and try to export to Latex PDF.

## Expected behavior

Be consistent with Pandoc and don't render incorrectly formatted math/latex as math text.

## Context

- Operating System and version: Linux Ubuntu 21.04
- Browser and version: Firefox 91.
- JupyterLab version: 3.0.16