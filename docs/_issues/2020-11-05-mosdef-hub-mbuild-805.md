---
tags: enhancement
title: "XYZ writer improvements"
html_url: "https://github.com/mosdef-hub/mbuild/issues/805"
user: rsdefever
repo: mosdef-hub/mbuild
---

I propose the following changes to the XYZ writer:

1. Switch to using <element> <x> <y> <z> instead of <atom_name> ... 
2. Allow a `mbuild.Compound` to be written to xyz rather than requiring a `parmed.Structure`
3. Support writing box information with the [extended XYZ spec](https://web.archive.org/web/20190811094343/https://libatoms.github.io/QUIP/io.html#extendedxyz)

Any others while we're at it? 
