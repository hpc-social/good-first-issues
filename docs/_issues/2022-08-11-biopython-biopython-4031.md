---
tags: Enhancement,help-wanted
title: "Bio.PDB.PSEA should use a temporary directory to run the third-party tool"
html_url: "https://github.com/biopython/biopython/issues/4031"
user: JoaoRodrigues
repo: biopython/biopython
---

Spun-off from #3999. `psea` should run in a temporary directory to avoid leaving unnecessary output files. For example:

```
def run_psea(...):
    curdir = os.path.abspath(os.curdir)
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        .... # run psea
        os.chdir(curdir)  # go back to where we started
```
        