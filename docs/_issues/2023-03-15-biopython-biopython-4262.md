---
title: "Replace print statements by warnings or stderr in NCBIXML"
html_url: "https://github.com/biopython/biopython/issues/4262"
user: JoaoRodrigues
repo: biopython/biopython
---

Follow-up to #4256, we should replace the print statements in the NCBIXML module by either calls to `warnings` or to `sys.stderr`, to be easier to ignore/discard.

Labelling this as a good first issue, but feel free to remove the label @peterjc.