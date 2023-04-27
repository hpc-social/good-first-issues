---
tags: enhancement,hdf4
title: "hdf_open - error reporting"
html_url: "https://github.com/gnudatalanguage/gdl/issues/712"
user: slayoo
repo: gnudatalanguage/gdl
---

```
IDL> a=hdf_open(/create)

a=hdf_open(/create)
                   ^
% HDF_OPEN: Incorrect number of arguments.
```

```
GDL> a=hdf_open(/create)
% HDF_OPEN: Variable is undefined: <Undefined>
% Execution halted at: $MAIN$  
```