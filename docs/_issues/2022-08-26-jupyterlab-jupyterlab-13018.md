---
tags: enhancement,pkgdebugger
title: "Debugger side bar not minimized when disabling the debugger"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/13018"
user: karlaspuldaro
repo: jupyterlab/jupyterlab
---

### Problem
When the debugger is enabled, the debugger side panel is expanded.
However, if one disables the debugger from the toolbar the side panel is currently not minimized, forcing the user to do that manually.

![image](https://user-images.githubusercontent.com/25207344/186985792-247f415c-de37-4bf8-9bfd-c49123e5cc87.png)

### Proposed Solution
Minimize the debugger side bar when the user disables the debugger.
