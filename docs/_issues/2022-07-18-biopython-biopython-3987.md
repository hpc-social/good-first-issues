---
tags: Bug,help-wanted
title: "Fix PDBList access to servers other than RCSB"
html_url: "https://github.com/biopython/biopython/issues/3987"
user: JoaoRodrigues
repo: biopython/biopython
---

In several places in `PDBList.py`, we try to build links to the databases expecting a url path of the form `/pub/pdb/...` (e.g. [here](https://github.com/JoaoRodrigues/biopython/blob/4d7042ed1185505691c7275c50bb539ef871211a/Bio/PDB/PDBList.py#L160)). While this works for RCSB (American site), it fails for the EBI (European) site because their urls expect `/pub/databases/pdb/...` (e.g. `https://ftp.ebi.ac.uk/pub/databases/pdb/data/status/latest/`).

This is an easy fix that involves changing the root (default) `self.pdb_server` address in our code to include the `/pub/` prefix and remove it from all the URLs we build. This would make it easier to change `self.pdb_server` tackle any of the 3 main mirrors of the database:
- https://ftp.ebi.ac.uk/pub/databases/pdb/data/status/latest/
- https://ftp.pdbj.org/pub/pdb/data/status/latest/
- https://ftp.rcsb.org/pub/pdb/data/status/latest/

This might break scripts that connect to PDBj and custom databases that follow the RCSB pattern and adapted to the script's use of /pub/ in the links. However, it does fix access to EBI, so I think it's an acceptable price to pay for an actual bug fix.

In addition, we could add a function to pick the fastest server automatically based on the user's connection/location, by measuing access to each server and picking the best (sample code [here](https://stackoverflow.com/questions/6159173/how-to-choose-closest-fastest-mirror-in-python)).