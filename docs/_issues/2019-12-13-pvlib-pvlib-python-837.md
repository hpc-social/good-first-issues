---
tags: ,documentation,help-wanted
title: "add call outs to all references in docstrings"
html_url: "https://github.com/pvlib/pvlib-python/issues/837"
user: wholmgren
repo: pvlib/pvlib-python
---

#833 converts all references into the numpydoc format. The unfortunate side effect of this is that it creates a lot of warnings in the sphinx build because many of the references are not called out in the docstring. #833 silences these warnings using `suppress_warnings = ['ref.footnote']`. In the long run, it would be great to call out the references and remove the suppress warnings statement. That would move us one step closer to automatically and comprehensively checking docstrings for style.