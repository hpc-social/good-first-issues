---
tags: ,RIA/ORA,enhancement
title: "RF AnnexRepo: extend/unify init_remote and enable_remote"
html_url: "https://github.com/datalad/datalad/issues/5062"
user: yarikoptic
repo: datalad/datalad
---

`datalad/distributed/tests/ria_utils.py` already has

```python
def initremote(repo, name, encryption=None, config=None):
    cfg = dict(config) if config else {}
    cfg['encryption'] = encryption if encryption else 'none'
    args = ['{}={}'.format(k, v) for k, v in cfg.items()]
    repo.init_remote(name, args)


def initexternalremote(repo, name, type, encryption=None, config=None):
    config = dict(
        config if config else {},
        type='external',
        externaltype=type,
    )
    return initremote(repo, name, encryption=encryption, config=config)
```
so IMHO we should just tune our existing `init_remote` and `enable_remote` to accept options given as a dict (and do above tune up), and `init_remote` get a kwargs `encryption=None`, `external=False`.  That would simplify use of `init_remote` and remove custom  (albeit generic) code in `datalad/distributed/tests/ria_utils.py`