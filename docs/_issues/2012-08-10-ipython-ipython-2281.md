---
tags: 
title: "Robust default color scheme"
html_url: "https://github.com/ipython/ipython/issues/2281"
user: dimaqq
repo: ipython/ipython
---

Currently there are 3 color schemes to choose from:
- linux, in which exceptions are unreadable in terminal with white background
- lightbg, in which exceptions are hard to read in terminal with black background
- nocolor, which has no colors

Other tools, e.g. GNU ls, manage to provide a default color scheme that's legible in both terminals with white and black backgrounds.

I would like to see ipython adopt similar default color scheme.

As far as I understand 2 bits are required:
- never use "set fg black" or "set fg white" escape sequences, rather use "reset fg" seq, and
- don't use very very light or very very dark colors.
