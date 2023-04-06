---
tags: 
title: "Add type hints to entity grid"
html_url: "https://github.com/dpalmasan/TRUNAJOD2.0/issues/17"
user: dpalmasan
repo: dpalmasan/TRUNAJOD2.0
---

The entity grid module can be found in the following source:

https://github.com/dpalmasan/TRUNAJOD2.0/blob/master/src/TRUNAJOD/entity_grid.py

For example, the function:

```python
def get_local_coherence(egrid):
```

Could be defined as:

```python
def get_local_coherence(egrid: EntityGrid) -> Tuple[float, float, float, float, float]:
```