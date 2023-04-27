---
tags: type/bug
title: "`verdi archive create --test-run` still claims to have written the archive"
html_url: "https://github.com/aiidateam/aiida-core/issues/5980"
user: mbercx
repo: aiidateam/aiida-core
---

### Describe the bug

Tiny bug, even when doing a test run there is still a statement at the end that an archive file is written:

```python
(aiida-sdb) aiida@prnmarvelsrv3:~/envs/aiida-sdb/data/archive$ verdi archive create --no-create-backward -G icsd/structure/stoichiometric  --test-run icsd-stoichiometric.aiida
Report: 
Archive Parameters
--------------------  -------------------------
Path                  icsd-stoichiometric.aiida
Version               main_0001
Compression           6

[...]

Report: Validating Nodes                                                                                                                                                                                                
Report: Test Run: Stopping before archive creation
Report: Archive would be created with:
----------------  ------
users                  1
groups                 1
nodes             106216
group_nodes       106216
Repository Files       0
----------------  ------
Success: wrote the export archive file to icsd-stoichiometric.aiida
```

### Expected behavior

Besides not printing the statement, I'm wondering: wasn't this called `--dry-run` before? I feel that terminology would be more consistent.

### Your environment

- Operating system [e.g. Linux]: Ubuntu 20.04.1 LTS
- Python version [e.g. 3.7.1]: Python 3.8.10
- aiida-core version [e.g. 1.2.1]: v2.3.0
