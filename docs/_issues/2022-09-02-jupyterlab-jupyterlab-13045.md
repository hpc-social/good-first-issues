---
tags: bug,pkgapputils,tagAccessibility
title: "ARIA labels on main area widget are incorrect (always referring to a notebook)"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/13045"
user: krassowski
repo: jupyterlab/jupyterlab
---

## Description

https://github.com/jupyterlab/jupyterlab/blob/b57ec962a7b8cda65bb89a72223f195564f8387a/packages/apputils/src/mainareawidget.ts#L46-L50

says "notebook content" when using a file editor or opening a CSV file, etc, but it should not.

We could:
- change it to "main area content" and "main area toolbar"
- in each of the `MainAreaWidget` subclasses set a proper text
  - we could take the string from a getter so subclasses have less work (getter so that we can translate)
  - if we want to be more strict we could use an abstract getter and force all subclasses of `MainAreaWidget` to provide an aria-label since 4.0
