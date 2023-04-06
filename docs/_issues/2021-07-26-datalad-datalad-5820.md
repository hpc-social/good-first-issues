---
tags: ,DX,easy
title: "Replace os.path imports with custom helper"
html_url: "https://github.com/datalad/datalad/issues/5820"
user: adswa
repo: datalad/datalad
---

In #5814 @yarikoptic noted that there is an alternative to ``os.path`` imports:

> we also have `datalad/support/path.py` which provides few extra functions but primarily a replacement for `os.path` imports with some guards added for unicode filenames handling.  I guess neither me nor anyone else switched to use it systematically and was doing imports `import datalad.support.path as op` only whenever running into unicode issues... surprisingly I find only a single import of such kind!
```shell
$> git grep 'import .*\.path.*as op' | grep -v 'os\.path'
datalad/plugin/addurls.py:import datalad.support.path as op
```
>but we do few direct ones:

```shell
$> git grep support.path -- datalad
datalad/customremotes/archives.py:from ..support.path import exists
datalad/customremotes/base.py:from ..support.path import exists, join as opj, dirname, lexists
datalad/distribution/tests/test_siblings.py:from datalad.support.path import (
datalad/interface/results.py:from datalad.support.path import robust_abspath
datalad/metadata/aggregate.py:from datalad.support.path import split_ext
datalad/plugin/addurls.py:import datalad.support.path as op
datalad/plugin/addurls.py:from datalad.support.path import split_ext
datalad/plugin/export_to_figshare.py:    from ..support.path import basename
datalad/support/archives.py:from datalad.support.path import (
``` 

> [...] think it might be worth to "solidify" that we use that helper submodule instead of `os.path`

Recording it here as a new issue to not loose the comment. 