---
tags: ,help-wanted
title: "Treat subprocess errors as exceptions"
html_url: "https://github.com/ipython/ipython/issues/9657"
user: minrk
repo: ipython/ipython
---

We do some things differently when an exception is met (e.g. abort queued tasks in the kernel). We should probably be treating subprocess errors (`!fail`, `%%script` magics) as exceptions in the same way, though we don't want to end up displaying a traceback.
