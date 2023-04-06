---
tags: ,documentation
title: "Documentation regarding input/output options"
html_url: "https://github.com/mosdef-hub/foyer/issues/81"
user: ctk3b
repo: mosdef-hub/foyer
---

Current inputs can come from mbuild, parmed or openmm topologies + an xml file.

By default `Forcefield.apply()` yields a parmed structure but for users interested in running in OpenMM we can also easily break out earlier. This needs to be tidied up a bit and properly documented.