---
tags: Enhancement,help-wanted
title: "Access to Alphafold database of 3D modules in a PDBList-like interface"
html_url: "https://github.com/biopython/biopython/issues/3990"
user: JoaoRodrigues
repo: biopython/biopython
---

This has been somewhat raised in #3853, but it would be potentially interesting to add a small interface to bulk (or not) download Alphafold models and build a structured database that users could keep updated, This module could be based off `PDBList.py` and could initially be limited to downloading structures by species, accession(s), but later on potentially allow for more complex queries. I could see this being a nice pipeline piece combined with our BLAST and PDB modules.