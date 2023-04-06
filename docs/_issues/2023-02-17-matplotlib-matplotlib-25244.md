---
tags: ,Difficulty-Medium,Good-first-issue
title: "[Bug]: DeprecationWarning for pkg_resources.declare_namespace usage in mpl_toolkit"
html_url: "https://github.com/matplotlib/matplotlib/issues/25244"
user: rjgildea
repo: matplotlib/matplotlib
---

### Bug summary

As of [setuptools v67.3.0](https://setuptools.pypa.io/en/latest/history.html#v67-3-0) the use of `pkg_resources.declare_namespace` in [`lib/mpl_toolkits/__init__.py`](https://github.com/matplotlib/matplotlib/blob/f6e0ee49c598f59c6e6cf4eefe473e4dc634a58a/lib/mpl_toolkits/__init__.py#L2) raises a `DeprecationWarning`.


### Code for reproduction

```python
$ mamba create -n test python=3.10 matplotlib-base -y
$ mamba activate test
$ export PYTHONDEVMODE=1
$ python -c "import pkg_resources"
```


### Actual outcome

```
/path/to/test/lib/python3.10/site-packages/pkg_resources/__init__.py:2804: DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('mpl_toolkits')`.
Implementing implicit namespace packages (as specified in PEP 420) is preferred to `pkg_resources.declare_namespace`. See https://setuptools.pypa.io/en/latest/references/keywords.html#keyword-namespace-packages
  declare_namespace(pkg)
```

### Expected outcome

No output

### Additional information

See also:
https://setuptools.pypa.io/en/latest/references/keywords.html#keyword-namespace-packages
https://packaging.python.org/en/latest/guides/packaging-namespace-packages/
https://peps.python.org/pep-0420/

### Operating system

_No response_

### Matplotlib Version

3.7.0

### Matplotlib Backend

TkAgg

### Python version

Python 3.10.9

### Jupyter version

_No response_

### Installation

conda