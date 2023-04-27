---
tags: bug,tagPerformance
title: "Command palette gets re-rendered even if hidden"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/13677"
user: krassowski
repo: jupyterlab/jupyterlab
---

## Description

Command palette gets re-rendered even if hidden.

## Reproduce

<!--Describe step-by-step instructions to reproduce the behavior-->

1. Open command palette and two tabs
2. Close the command palette
3. Go to inspector right click on command palette element, select "break on" > "subtree modifications"
4. Switch tabs
5. See that command palette fragments get re-rendered via lumino virtual DOM

![Screenshot from 2022-12-29 13-23-55](https://user-images.githubusercontent.com/5832902/209961278-164071f9-3032-4091-af3e-84102658cbcb.png)

It is not clear to me why this update appears. Of note the migration to `requestAnimationFrame` in lumino seems to make the debugging/profiling a bit more confusing as I don't immediately see if this was a genuine animation frame request or just lumino messaging.

## Expected behavior

Updating command palette on tab switch is expected because different commands will become available in different contexts (e.g. text editor/notebook), but re-rendering it while it is hidden is not expected.

In a bigger picture we could ask: should command palette get detached rather than hidden. I think hiding is ok because there is ever only one command palette, but requires a better hygiene on when a re-render is triggered.

## Context

- JupyterLab version: 4.0.0a31