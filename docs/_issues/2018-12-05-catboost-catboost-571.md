---
tags: help-wanted
title: "Add option for auto None & nan imputation for categorical features"
html_url: "https://github.com/catboost/catboost/issues/571"
user: chanansh
repo: catboost/catboost
---

Feature Request:
Catboost should handle nan categorical features, e.g. via marking it as a special categorical entry "Unknown" or via Mode Imputation.
current state produces an error:
```
CatBoostClassifier().fit(pd.DataFrame({'cat_feature':['USA','ILS','CAD',pd.np.nan]}), [1,1,0,0], cat_features=[0])
Traceback (most recent call last):
  File "_catboost.pyx", line 1141, in _catboost._PoolBase._set_data_from_generic_matrix
  File "_catboost.pyx", line 840, in _catboost.get_id_object_bytes_string_representation
_catboost.CatboostError: bad object for id: nan
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "/home/hanans/.conda/envs/retarget/lib/python3.6/site-packages/catboost/core.py", line 2153, in fit
    silent, early_stopping_rounds, save_snapshot, snapshot_file, snapshot_interval)
  File "/home/hanans/.conda/envs/retarget/lib/python3.6/site-packages/catboost/core.py", line 1090, in _fit
    train_pool = _build_train_pool(X, y, cat_features, pairs, sample_weight, group_id, group_weight, subgroup_id, pairs_weight, baseline, column_description)
  File "/home/hanans/.conda/envs/retarget/lib/python3.6/site-packages/catboost/core.py", line 656, in _build_train_pool
    group_weight=group_weight, subgroup_id=subgroup_id, pairs_weight=pairs_weight, baseline=baseline)
  File "/home/hanans/.conda/envs/retarget/lib/python3.6/site-packages/catboost/core.py", line 286, in __init__
    self._init(data, label, cat_features, pairs, weight, group_id, group_weight, subgroup_id, pairs_weight, baseline, feature_names)
  File "/home/hanans/.conda/envs/retarget/lib/python3.6/site-packages/catboost/core.py", line 637, in _init
    self._init_pool(data, label, cat_features, pairs, weight, group_id, group_weight, subgroup_id, pairs_weight, baseline, feature_names)
  File "_catboost.pyx", line 1032, in _catboost._PoolBase._init_pool
  File "_catboost.pyx", line 1038, in _catboost._PoolBase._init_pool
  File "_catboost.pyx", line 1161, in _catboost._PoolBase._set_data_and_feature_names
  File "_catboost.pyx", line 1143, in _catboost._PoolBase._set_data_from_generic_matrix
_catboost.CatboostError: Invalid type for cat_feature[3,0]=nan : cat_features must be integer or string, real number values and NaN values should be converted to string.

```
catboost version: '0.11.1'
Operating System: Linux
CPU: Intel
GPU: None