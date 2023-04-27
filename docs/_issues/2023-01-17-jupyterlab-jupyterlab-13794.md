---
tags: maintenance
title: "Please switch from pytest-tornasync to pytest-jupyter"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/13794"
user: frenzymadness
repo: jupyterlab/jupyterlab
---

Would it be possible to remove the dependency on tornasync?

https://github.com/jupyterlab/jupyterlab/blob/d4688fe784c2b7d8cb9af8a153af88c91fd8dcc8/pyproject.toml#L109

pytest-tornasync is dead upstream and pytest-jupyter contains some of its important pieces so you no longer need it, see https://github.com/jupyter-server/pytest-jupyter/commit/10cf9ca3f7256e9793059838a5d2acc9763ab982

Also, jupyter-server-terminals already switched and it seems to be easy, see https://github.com/jupyter-server/jupyter_server_terminals/commit/744451298913d2c2d81698f94d16dfb595df897f 

My motivation for this request is that I'm trying to package Jupyter Lab and the latest Notebook into Fedora Linux and packaging unmaintained projects like tornasync is a bad idea.