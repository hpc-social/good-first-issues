---
tags: bug,documentation,tagDocumentation
title: "extension-cookiecutter-ts out of sync with doc."
html_url: "https://github.com/jupyterlab/jupyterlab/issues/12388"
user: Carreau
repo: jupyterlab/jupyterlab
---

https://github.com/jupyterlab/extension-cookiecutter-ts uses `const plugin: JupyterFrontEndPlugin<...` while all the documentation on getting started are using `const extension...` so if anyone copy past, you may get non-working code. As the getting started recommend to us the cookie cutter, it would be nice to have it synced