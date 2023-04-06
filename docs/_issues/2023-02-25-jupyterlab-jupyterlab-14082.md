---
tags: ,bug
title: "Running sessions status bar title does not work"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/14082"
user: krassowski
repo: jupyterlab/jupyterlab
---

## Description

This statusbar item:

![Screenshot from 2023-02-25 16-30-36](https://user-images.githubusercontent.com/5832902/221368375-bc6e7d19-8b83-41e6-b83f-0c3c38a20043.png)

1) Does not show title when hovering over it even though we set it here:

    https://github.com/jupyterlab/jupyterlab/blob/830931dead61c78dbc5ab12cafd6a8d2e280a75d/packages/apputils/src/runningSessions.tsx#L115-L126
   This is a result of incorrect React-Lumino mix-up.

2) The title translator has a typo: `jupyterload` vs `jupyterlab`:
    https://github.com/jupyterlab/jupyterlab/blob/830931dead61c78dbc5ab12cafd6a8d2e280a75d/packages/apputils/src/runningSessions.tsx#L92

## Context

- JupyterLab version: 4.0.0a32
