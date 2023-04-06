---
tags: ,Difficulty-Medium,Good-first-issue
title: "[Bug]: crash due to backend issue in ipython session started explicitly with InteractiveShell "
html_url: "https://github.com/matplotlib/matplotlib/issues/23770"
user: zpincus
repo: matplotlib/matplotlib
---

### Bug summary

If an IPython session is started via `IPython.core.interactiveshell.InteractiveShell.instance()`, trying to create a matplotlib figure, or even query the backend, produces a crash (stack trace below) on OS X, and on Linux if there is an active X11 session.

Without an X session on Linux or if ipython is started via the command-line `ipython` command, everything works as expected.

### Code for reproduction

```python
import IPython.core.interactiveshell
IPython.core.interactiveshell.InteractiveShell.instance()

import matplotlib.pyplot
matplotlib.pyplot.figure()
# or the below crashes too
import matplotlib
matplotlib.get_backend()
```


### Actual outcome

```
In : matplotlib.pyplot.figure()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/matplotlib/pyplot.py", line 806, in figure
    manager = new_figure_manager(
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/matplotlib/pyplot.py", line 324, in new_figure_manager
    _warn_if_gui_out_of_main_thread()
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/matplotlib/pyplot.py", line 314, in _warn_if_gui_out_of_main_thread
    if (_get_required_interactive_framework(_get_backend_mod())
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/matplotlib/pyplot.py", line 217, in _get_backend_mod
    switch_backend(dict.__getitem__(rcParams, "backend"))
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/matplotlib/pyplot.py", line 262, in switch_backend
    switch_backend(candidate)
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/matplotlib/pyplot.py", line 310, in switch_backend
    install_repl_displayhook()
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/matplotlib/pyplot.py", line 150, in install_repl_displayhook
    ip.enable_gui(ipython_gui_name)
  File "/Users/zpincus/miniconda/envs/mplcrash/lib/python3.10/site-packages/IPython/core/interactiveshell.py", line 3455, in enable_gui
    raise NotImplementedError('Implement enable_gui in a subclass')
NotImplementedError: Implement enable_gui in a subclass

```

### Expected outcome

```
In : matplotlib.pyplot.figure()
<Figure size 640x480 with 0 Axes>
```

### Additional information

The below is sufficient to reproduce the crash from a clean environment. 
```
conda create -n "mplcrash" -c conda-forge python=3.10 matplotlib ipython
conda activate mplcrash
python -c 'import IPython.core.interactiveshell as ipsh; ipsh.InteractiveShell.instance(); import matplotlib.pyplot as plt; plt.figure()'
```

It's a weird corner case to be creating an ipython session this way, and perhaps the problem is on my end, but I wasn't expecting a crash like this regardless...

### Operating system

macOS, Linux, maybe windows too?

### Matplotlib Version

3.5.3

### Matplotlib Backend

this crashes too with the same error when invoked after starting `InteractiveShell.instance()` 

### Python version

3.10.6 (but also occurs with various 3.9 versions)

### Jupyter version

_No response_

### Installation

conda