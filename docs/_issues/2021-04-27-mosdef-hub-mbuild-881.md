---
tags: 
title: "Improve box handling in pybel tests"
html_url: "https://github.com/mosdef-hub/mbuild/issues/881"
user: jennyfothergill
repo: mosdef-hub/mbuild
---

TODO comments from `mbuild/tests/test_compound.py`
```
1161-    def test_from_pybel_molecule(self, extension):
1162-        pybel = import_('pybel')
1163-        chol = list(pybel.readfile(extension,
1164-            get_fn('cholesterol.{}'.format(extension))))[0]
1165:        # TODO: Actually store the box information
```
related to #872