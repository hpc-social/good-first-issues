---
title: "Improve handling of PBC info from openbabel"
html_url: "https://github.com/mosdef-hub/mbuild/issues/880"
user: jennyfothergill
repo: mosdef-hub/mbuild
---

TODO comments from `mbuild/conversion.py`
```
769-        if not ignore_box_warn:
770-            warn("No unitcell detected for pybel.Molecule {}".format(pybel_mol))
771:#       TODO: Decide how to gather PBC information from openbabel. Options may
772-#             include storing it in .periodicity or writing a separate function
773-#             that returns the box.
```
related to #872

