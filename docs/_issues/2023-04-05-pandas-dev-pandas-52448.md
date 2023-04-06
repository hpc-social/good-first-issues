---
tags: ,Code-Style
title: "STYLE use TypeAlias and upgrade ruff"
html_url: "https://github.com/pandas-dev/pandas/issues/52448"
user: MarcoGorelli
repo: pandas-dev/pandas
---

The latest autoupdate job removes some useful type aliases definitions

As noted by @twoertwein , this is because we haven't annotated them as `TypeAlias`

So, the task here is:
1. `pre-commit autoupdate`
2. add
```
  # Useless statement
  "B018",
```
under `Additional checks that don't pass yet` in `pyproject.toml`

3. check which files were updated in https://github.com/pandas-dev/pandas/pull/52345/files . For any place where the type alias definition was replaced with `...`, you should annotate the variable with `TypeAlias`

Here's an example of the kind of change you'd be making:
```diff
diff --git a/pandas/_libs/interval.pyi b/pandas/_libs/interval.pyi
index 4c36246e04..f0412b8397 100644
--- a/pandas/_libs/interval.pyi
+++ b/pandas/_libs/interval.pyi
@@ -3,6 +3,7 @@ from typing import (
     Generic,
     TypeVar,
     overload,
+    TypeAlias,
 )
 
 import numpy as np
@@ -16,9 +17,9 @@ from pandas._typing import (
 
 VALID_CLOSED: frozenset[str]
 
-_OrderableScalarT = TypeVar("_OrderableScalarT", int, float)
-_OrderableTimesT = TypeVar("_OrderableTimesT", Timestamp, Timedelta)
-_OrderableT = TypeVar("_OrderableT", int, float, Timestamp, Timedelta)
+_OrderableScalarT: TypeAlias = TypeVar("_OrderableScalarT", int, float)
+_OrderableTimesT: TypeAlias = TypeVar("_OrderableTimesT", Timestamp, Timedelta)
+_OrderableT: TypeAlias = TypeVar("_OrderableT", int, float, Timestamp, Timedelta)
 
 class _LengthDescriptor:
     @overload
```

4. run `pre-commit run ruff --all-files`, and check that no type alias definitions are overwritten by `...`
5. run `pre-commit run --all-files`, check everything passes
6. stage, commit, open pull request

See the contributing guide for how to get started https://pandas.pydata.org/docs/dev/development/contributing.html