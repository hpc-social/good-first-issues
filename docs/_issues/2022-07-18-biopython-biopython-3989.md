---
tags: Enhancement,help-wanted
title: "Update argument handling in PDBList.py, possibly by creating a new module."
html_url: "https://github.com/biopython/biopython/issues/3989"
user: JoaoRodrigues
repo: biopython/biopython
---

The command-line interface for the `PDBList.py` module is quite clunky, using a series of complicated ifs and sys.argv calls to parse input from the user. It would be super nicer to simply use `argparse`, although this will break compatibility with previous versions.

The solution here might pass through copying the code to a new module and along with other issues (#3988, #3987) upgrade `PDBList.py` and break backwards compability. We could then slap a deprecation warning on PDBList to warn users to move to the new code.