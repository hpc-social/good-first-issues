---
tags: Testing
title: "silence warnings PDBConstructionWarning in test_PDB_StructureAlignment.py"
html_url: "https://github.com/biopython/biopython/issues/1877"
user: peterjc
repo: biopython/biopython
---

### Setup

Seen with latest code from git while preparing the 1.73 release on Linux, but applies to all platforms.

### Expected behaviour

```
$ python run_tests.py test_PDB_StructureAlignment.py
Python version: 2.7.15 | packaged by conda-forge | (default, Jul 27 2018, 10:26:36) 
[GCC 4.8.2 20140120 (Red Hat 4.8.2-15)]
Operating system: posix linux2
test_PDB_StructureAlignment ... ok
----------------------------------------------------------------------
Ran 1 test in 0.958 seconds
```

### Actual behaviour

```
$ python run_tests.py test_PDB_StructureAlignment.py
Python version: 2.7.15 | packaged by conda-forge | (default, Jul 27 2018, 10:26:36) 
[GCC 4.8.2 20140120 (Red Hat 4.8.2-15)]
Operating system: posix linux2
test_PDB_StructureAlignment ... /tmp/biopython-1.73/build/lib.linux-x86_64-2.7/Bio/PDB/StructureBuilder.py:91: PDBConstructionWarning: WARNING: Chain A is discontinuous at line 13298.
  PDBConstructionWarning)
/tmp/biopython-1.73/build/lib.linux-x86_64-2.7/Bio/PDB/StructureBuilder.py:91: PDBConstructionWarning: WARNING: Chain B is discontinuous at line 13344.
  PDBConstructionWarning)
ok
----------------------------------------------------------------------
Ran 1 test in 0.958 seconds
```

### Steps to reproduce

Use ``python run_tests.py --offline test_PDB_StructureAlignment.py`` or similar.

We need to catch and ignore the ``PDBConstructionWarning`` here, see for example:

https://github.com/biopython/biopython/blob/biopython-172/Tests/test_PDB.py#L107

i.e. Wrap as few lines as possible in the context manager
