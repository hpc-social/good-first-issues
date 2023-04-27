---
tags: Bug,Enhancement,help-wanted
title: "Extend PDBList obsolete handling to mmCIF and mmtf formats as well as assemblies"
html_url: "https://github.com/biopython/biopython/issues/3988"
user: JoaoRodrigues
repo: biopython/biopython
---

The current code in `PDBList.py` to move obsolete files expects a `.ent` extension, which is reserved for PDB-formatted files. We should extend this to depend on the file_format of choice (e,g. mmCIF, mmtf) and also to assemblies (if the original entry is labelled obsolete). Relevant code is [here](https://github.com/JoaoRodrigues/biopython/blob/4d7042ed1185505691c7275c50bb539ef871211a/Bio/PDB/PDBList.py#L389).

Fixing this involves keeping track of which extensions are used for which file formats, probably by encoding a dictionary to map file_format to extension, and then retrieving the extension based on the file_format provided to `update_pdb`.

