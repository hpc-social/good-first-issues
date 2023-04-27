---
title: "NameError/AttributeError suggestions in Python 3.10 error messages"
html_url: "https://github.com/ipython/ipython/issues/13445"
user: tirkarthi
repo: ipython/ipython
---

Python 3.10 added suggestions for AttributeError and NameError in the error messages. It seems the suggestions are not stored in the exception object but calculated when Error is displayed. There is a note that that this won't work with IPython but it will be good to see if it's feasible. Opening an issue for discussion.

https://bugs.python.org/issue38530 
https://docs.python.org/3/whatsnew/3.10.html#attributeerrors 

Discussion on HN : https://news.ycombinator.com/item?id=29909799