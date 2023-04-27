---
tags: UX/DX
title: "Implement `_repr_html_` on relevant classes"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/1012"
user: sk1p
repo: LiberTEM/LiberTEM
---

`_repr_html_` is used by Jupyter notebooks to display rich information on objects. This could be a nice way of improving LiberTEM usage in notebooks. Right now, I can think of:

- `ResultBuffer` - mainly useful if a user just types `udf_results['some_buffer']` in their notebook - we can show shape/dtype/... but also hint at usage, like `.data` and `.raw_data`, including `__array__`.
- `DataSet` - may need tweaks for each dataset impl, don't know...
- `Context` - information about the executor/cluster we are connected to