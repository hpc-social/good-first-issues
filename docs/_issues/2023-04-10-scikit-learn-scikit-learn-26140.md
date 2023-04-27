---
tags: Bug,help-wanted,moduleensemble
title: "RandomForest not passing feature names to trees and creating warnings."
html_url: "https://github.com/scikit-learn/scikit-learn/issues/26140"
user: howarth
repo: scikit-learn/scikit-learn
---

### Describe the bug

I fit a decision forest with training data that includes feature names. When I call predict_proba on the forest everything is fine. When I call rf.estimators_[0].predict_proba it will warn that it was not trained with feature names.


### Steps/Code to Reproduce
```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

print(sklearn.__version__)

data = np.random.normal([1,2,3,4,5,6,7,8,9,10], size=(1000, 10))
feature_names = [f'F{i}' for i in range(10)]
df = pd.DataFrame(data=data, columns=feature_names)
y = np.ones(1000)
y[500:] = 0

rf = RandomForestClassifier()
rf.fit(df, y)

print(f"Feature names in Forest: {rf.feature_names_in_} ")

print('Classing pred proba on forest')
rf.predict_proba(df)
print('Done calling pred proba on forest')

# THIS GIVES A WARNING
rf.estimators_[0].predict_proba(df)
```

### Expected Results

No warnings

### Actual Results
```
Feature names in Forest: ['F0' 'F1' 'F2' 'F3' 'F4' 'F5' 'F6' 'F7' 'F8' 'F9'] 
Classing pred proba on forest
Done calling pred proba on forest
.....lib/python3.8/site-packages/sklearn/base.py:432: UserWarning: X has feature names, but DecisionTreeClassifier was fitted without feature names
  warnings.warn(
```
### Versions

```shell
sk>>> sklearn.show_versions()

System:
    python: 3.8.16 (default, Mar  2 2023, 03:21:46)  [GCC 11.2.0]
executable: ....../bin/python
   machine: Linux-5.15.0-60-generic-x86_64-with-glibc2.17

Python dependencies:
      sklearn: 1.2.2
          pip: 23.0.1
   setuptools: 65.6.3
        numpy: 1.23.1
        scipy: 1.9.0
       Cython: None
       pandas: 1.5.3
   matplotlib: None
       joblib: 1.1.1
threadpoolctl: 2.2.0
```
