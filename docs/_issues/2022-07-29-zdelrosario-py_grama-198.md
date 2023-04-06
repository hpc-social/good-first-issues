---
tags: ,enhancement
title: "Missing documentation / docstrings"
html_url: "https://github.com/zdelrosario/py_grama/issues/198"
user: mstites
repo: zdelrosario/py_grama
---

While working on the readthedocs submodule issue (#181), I observed that there were a number of user accessible functions that didn't have docstrings. While most of these were pretty self explanatory functions, it would be nice to have more information and documentation coverage available to the user.

I went through all the readthedocs documentation pages  while simultaneously scrolling through the code. I observed the following functions have no (or limited) docstrings:
- Plot_auto: plot_corrtile
- Grama.tools: add_pipe, custom_format_warning, pipe
- Grama.string_helpers: all exist, some could just use longer docstrings. What arguments? Results? Examples?
- Grama.marginals: marginal_helpers needs elaboration in my opinion
- Grama.modules: circuit_RLS,mark_prlc, circuit_RLC.make_PRLC_rand, Linear_norminal, plane_lamite, & more.

**These functions should be given docstrrings to match the rest of the package. Priority should be for less self explanatory functions such as plot_corrtile. In general, grama needs more examples that demonstrate both the core functionality and edge functionality of functions.** 

Even if the functions seem self explanatory, documentation should be given as functions without documentation can confuse the user. For example, add_pipe is pretty basic functionality, and not one the user has to think much about. But documenting his more would give more intuition into how grama functions and how to use it. This also reduces "unknowns" for when users are troubleshooting. We should compare our docstrings to other packages in the same realm of functionality such as pandas, scipy, numpy, etc. 