---
tags: ,bug,pkgcompleter,pkgdocumentsearch
title: "Both completer and document search event handlers get dispatched on Esc"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/13659"
user: krassowski
repo: jupyterlab/jupyterlab
---

## Description

`Cannot execute key binding 'Escape': command 'documentsearch:end' is not enabled.` shows up when closing completer with <kbd>Esc</kbd> in file editor

## Reproduce

1. Open text editor with python file
2. Invoke completer
3. Press Esc
4. See error in browser console

## Expected behavior

- completer widget cancels event if handled
- document search selector is more specific selecting only documents with open search view

## Context

- Browser and version: Chrome 108
- JupyterLab version: 4.0.0a31
