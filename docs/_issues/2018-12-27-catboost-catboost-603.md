---
tags: ,help-wanted
title: "Need to pass again cat_features in eval_metrics whereas it was already passed in CatBoostClassifier"
html_url: "https://github.com/catboost/catboost/issues/603"
user: ismael-elatifi
repo: catboost/catboost
---

catboost version: 0.12.0
Operating System: Windows

The issue is described and demonstrated by the code below.

```Python
from catboost import CatBoostClassifier, Pool
    
col_cat = ['A','B']
target =  [ 1,  0]
model = CatBoostClassifier(num_trees=1, depth=1, cat_features=[0])
model.fit(col_cat, target)
model.eval_metrics(Pool(col_cat, label=target, cat_features=[0]), metrics=["Accuracy"])
```
If we don't pass cat_features to eval_metrics, we get error :

> Bad value for num_feature[0,0]="A": Cannot convert 'b'A'' to float

cat_features is already passed to the model constructor CatBoostClassifier so it should not be necessary to pass it again in eval_metrics call