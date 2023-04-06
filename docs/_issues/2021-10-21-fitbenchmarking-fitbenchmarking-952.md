---
tags: ,Enhancement,Good-first-issue,Maintenance
title: "Change build system to use newer pyproject.toml approach"
html_url: "https://github.com/fitbenchmarking/fitbenchmarking/issues/952"
user: AndrewLister-STFC
repo: fitbenchmarking/fitbenchmarking
---

The setup.py approach to building a package is being(has been?) superceeded by declarative project definitions. In particular, [PEP261](https://www.python.org/dev/peps/pep-0621/) introduces the `pyproject.toml` file and this is starting to become what the "build-backends" are aiming to support.

For our purpose I don't know that the backend matters much? But I found that flit and trampolim which seem to be 2 relatively popular(?) options support it, whereas setuptools and Poetry are still debating how best to alter their metadata definitions.

Some examples of what build backends suggest:
- https://setuptools.pypa.io/en/latest/userguide/quickstart.html
- https://github.com/FFY00/trampolim
- https://flit.readthedocs.io/en/latest/pyproject_toml.html
- https://python-poetry.org/docs/pyproject/