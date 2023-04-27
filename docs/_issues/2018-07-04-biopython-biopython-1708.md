---
tags: Documentation
title: "PAML run method docstrings - return value"
html_url: "https://github.com/biopython/biopython/issues/1708"
user: peterjc
repo: biopython/biopython
---

The docstrings for the PAML run methods seem a little confusing/out-of-date about the return values.

https://github.com/biopython/biopython/blob/biopython-172/Bio/Phylo/PAML/_paml.py#L88
*"Return a process signal so the user can determine if the execution was successful (return code 0 is successful, -N indicates a failure)."*
Actually returns None, but will raise an exception if the return code was non-zero.

https://github.com/biopython/biopython/blob/biopython-172/Bio/Phylo/PAML/codeml.py#L172
https://github.com/biopython/biopython/blob/biopython-172/Bio/Phylo/PAML/baseml.py#L160
*"Return a process signal so the user can determine if the execution was successful (return code 0 is successful, -N indicates a failure)."*
Actually returns the parsed data, or None if parse=False. Again, should raise an exception if the return code was non-zero.

https://github.com/biopython/biopython/blob/biopython-172/Bio/Phylo/PAML/yn00.py#L97
Missing a docstring, but behaves as above.

Could you look at this please @brandoninvergo - even just to confirm my reading of the code, then we can tag this as an easy-fix issue for a potential new contributor to tackle.