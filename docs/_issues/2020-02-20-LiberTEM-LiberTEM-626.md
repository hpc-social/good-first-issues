---
tags: ,UX/DX,design,docs
title: "Improve interface for AUX data"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/626"
user: uellue
repo: LiberTEM/LiberTEM
---

Discussion with @sk1p and @Brow71189:

Currently, UDF users have to declare AUX data explicitly when constructing an UDF. This can make using a built-in UDF with aux data unnecessarily complicated.

A cleaner solution could be to implement wrapping parameters in the constructor. That means an UDF implements a specific `__init__` function with dedicated parameters instead of the default catch-all. That is emerging as good practice for documentation purposes anyway. Users pass plain NumPy arrays as specific parameters to the constructor, following the signature and documentation of the UDF. The UDF's constructor then wraps parameters in an AUX buffer as needed and handles them, for example by passing them up to the superclasse's constructor. One just has to take care about parameters being passed again on the worker nodes.