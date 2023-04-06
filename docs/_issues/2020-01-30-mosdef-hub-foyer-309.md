---
tags: ,testing
title: "Unify files used in force field validation"
html_url: "https://github.com/mosdef-hub/foyer/issues/309"
user: mattwthompson
repo: mosdef-hub/foyer
---

**Describe the behavior you would like added to Foyer**
Right now, in `test_opls.py`, the script crawls through a directory and tries to find either a combination of TOP & GRO files or a MOL2 file for each molecule. The latter, I believe, are there for legacy reasons; I'm pretty sure the files that Christoph started building this test suite out of were GROMACS files. But MOL2 files contain all the information we need (atom data, including atom types, and bonded connectivity) for atom-typing tests. I don't think a strictly enforced standard for reference files in atom-typing tests is necessary, but I think some commonality is useful.

**Describe the solution you'd like**
In [this](https://github.com/mosdef-hub/foyer/blob/5790b068907b9aec38fe2964937aaabca82e3a48/foyer/tests/test_opls.py#L50-L60) folder, convert every TOP/GRO pair to a MOL2 file. **NOTE:** we can write a little script to use ParmEd or other glue to automate this in a few seconds, but my trust in the conversion is close to 99.99%, so I believe it is appropriate to do this semi-manually. At very least, I believe it is necessary to check most of the details of the MOL2 file by hand (type, element, and bonded information at minimum).


**Describe alternatives you've considered**
As noted above, we could automate this, but it's plausibly incorrect for a small number of molecules.

**Additional context**
It is still my opinion that this testing should happen in other repos, but I am raising the issue here since we can have a discussion about how to standardize these tests.