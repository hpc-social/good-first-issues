---
tags: ,enhancement
title: "A GUI for creating MOOPs"
html_url: "https://github.com/parmoo/parmoo/issues/26"
user: thchang
repo: parmoo/parmoo
---

Not all users are comfortable working in Python, and ParMOO's interface is necessarily complicated.

We should build a GUI interface (for example, using ``tkinter`` or a web-interface), which allows users to:
 - define a MOOP and add problem components graphically (and guided by pop-ups/instructions from the GUI)
 - define their solver and solver/options graphically by browsing options in the current library/global scope,
 - choose parallel or serial options and activate checkpointing/logging, and then
 - export a Python script for running their problem.