---
tags: ,bug
title: "Custom c++ metric Run Problem"
html_url: "https://github.com/catboost/catboost/issues/1337"
user: gavrenkov
repo: catboost/catboost
---

Problem:
catboost version: 0.23.2
Operating System: all
Tutorial: https://github.com/catboost/tutorials/blob/master/custom_loss/custom_metric_tutorial.md

Impossible to use custom metric (С++). 

![image](https://user-images.githubusercontent.com/2998194/84900930-73ffcd00-b0b3-11ea-86d9-988ee84f8561.png)

**Code example**
```
from catboost import CatBoost
train_data = [[1, 4, 5, 6],
              [4, 5, 6, 7],
              [30, 40, 50, 60]]

eval_data = [[2, 4, 6, 8],
             [1, 4, 50, 60]]
train_labels = [10, 20, 30]
model = CatBoost(params={"loss_function":"UserPerObjMetric",'leaf_estimation_backtracking': 'No','eval_metric':'RMSE'})
model.fit(train_data, train_labels)
preds = model.predict(eval_data)

```

![image](https://user-images.githubusercontent.com/2998194/84903305-9810dd80-b0b6-11ea-81c5-aaf04b7d57de.png)

