---
tags: 
title: "[FEATURE] specify number of trees for shap"
html_url: "https://github.com/catboost/catboost/issues/1535"
user: pseudotensor
repo: catboost/catboost
---

Problem: the approximate method can still be slow for many trees
catboost version: master
Operating System: ubuntu 18.04
CPU: i9
GPU: RTX2080

Would be good to be able to specify how many trees to use for shapley.  The model.predict and prediction_type versions allow this.  lgbm/xgb allow this.
