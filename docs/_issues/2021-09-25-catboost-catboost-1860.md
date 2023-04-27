---
tags: help-wanted
title: "can we add namespace when save_model in format cpp?"
html_url: "https://github.com/catboost/catboost/issues/1860"
user: nickhuangxinyu
repo: catboost/catboost
---

usually, after trained model. i save model in cpp format with code:

```
cat_model.save_model('a', format="cpp")
cat_model.save_model('b', format="cpp")

```
but when my cpp need to use multi models.

in my main.cpp

```
#include "a.hpp"
#include "b.hpp"

int main() {
  // do something
  double a_pv = ApplyCatboostModel({1.2, 2.3});  // i want to a.hpp's model here
  double b_pv = ApplyCatboostModel({1.2, 2.3});  // b.hpp's here
}
```

this will be failed, because the function `ApplyCatboostModel `will be conflicit for duplicate function name.

could you add namespace in the api function `save_model`?