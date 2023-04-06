---
tags: ,Difficulty-Medium,GUI-MacOSX,GUI-tk,Good-first-issue
title: "option+letter on OSX with tkagg give non-alpha numeric rather than alt-<letter>"
html_url: "https://github.com/matplotlib/matplotlib/issues/22934"
user: tacaswell
repo: matplotlib/matplotlib
---

This issue is restricted to:
 - tk backend
 - on OSX



https://github.com/matplotlib/matplotlib/blob/1ab4a53d1cce6a8692d5439660f292683f4f7296/lib/matplotlib/backends/_backend_tk.py#L179

to

https://github.com/matplotlib/matplotlib/blob/1ab4a53d1cce6a8692d5439660f292683f4f7296/lib/matplotlib/backends/_backend_tk.py#L356-L358

to 

https://github.com/matplotlib/matplotlib/blob/1ab4a53d1cce6a8692d5439660f292683f4f7296/lib/matplotlib/backends/_backend_tk.py#L317-L352

is the call chain on our side.  This makes me think that the conversion is happening before it gets to us (but someone with a mac should probably verify that).


_Originally posted by @tacaswell in https://github.com/matplotlib/matplotlib/issues/22681#issuecomment-1111344498_