---
tags: enhancement,up-for-grabs
title: "Apply `mypy` typing checker to all files"
html_url: "https://github.com/BiomedSciAI/fuse-med-ml/issues/186"
user: SagiPolaczek
repo: BiomedSciAI/fuse-med-ml
---

**Is your feature request related to a problem? Please describe.**
As described [here](https://github.com/BiomedSciAI/fuse-med-ml/discussions/130), we use `black`, `flake8` and `mypy` to enforce certain format criteria.
Currently we are ignoring some of the issues and some of files for the `mypy` checker. See `./.mypy.ini` file for more details.

**Describe the solution you'd like**
Apply static typing in the ignored files so `mypy` will pass without ignoring any files (or at least much smaller amount).

**NOTES**
1. NO LOGIC SHOULD BE CHANGED. Only the static typing according the functions/classes properties.
2. This task might take too much time and effort in one-shot, so it can be done in a small doses - each PR with some amount of files fixed.
