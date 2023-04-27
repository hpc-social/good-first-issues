---
tags: symbolic
title: "Christoffel Symbols are no tensor!"
html_url: "https://github.com/einsteinpy/einsteinpy/issues/497"
user: andi8086
repo: einsteinpy/einsteinpy
---

🐞 Christoffel-Symbols are treated like tensors by API

For formatting or internal handling or whatever, we have
ch = ChristoffelSymbols.from_metric(m_obj)
ch.tensor()

🎯 Maybe better say Matrix instead of Tensor in this case

Tensors are multilinear maps. Just because something can be written
as a matrix does not mean it is a tensor.

It is very dangerous to refer to quantities as tensor if they are not, i.e.
follow a different coordinate transformation rule...

A tensor is a geometric object, i.e. if null it is null in all coordinate systems. The
christoffel symbols however can espacially transformed away in a free falling
reference frame. That would never be possible with a tensor.

This can cause a lot of confusion especially for students that use this software.
