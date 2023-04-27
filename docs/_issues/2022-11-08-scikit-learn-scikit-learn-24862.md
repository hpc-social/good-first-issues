---
tags: Meta-issue,Sprint,Validation
title: "Make automatic validation for all scikit-learn public functions"
html_url: "https://github.com/scikit-learn/scikit-learn/issues/24862"
user: glemaitre
repo: scikit-learn/scikit-learn
---

PR #22722 introduced a decorator to validate the parameters of functions. We now need to use it for all functions where it is applicable.

Please open one PR per function. The title of the PR must mention which function it's dealing with. We recommend using the following pattern for titles:

```
MAINT Parameters validation for <function>
```

where `<function>` is a placeholder to be replaced with the function you chose.

The description of the PR must begin with `Towards #24862` so that this issue and the PR are mutually crossed-linked.

### Steps

1. Chose a public function that is documented in https://scikit-learn.org/dev/modules/classes.html. Check in the source code if the function contains some manual parameter validation (i.e. you should see some `if` condition and error raising). In case there is no validation in the function, you can report it in the issue where we will decide whether or not to skip the function.

2. To validate the function, you need to decorate it with the decorator `sklearn.utils._param_validation.validate_params`. **Do not rely only on the docstring of the estimator to define it**: although it can help, it's important to primarily rely on the implementation to find the valid values because the docstring might not be completely accurate. The decorator take a Python dictionary as input where each key corresponds to a parameter name and the value corresponds to the associate constraints. You can find an example for `kmeans_plusplus` below https://github.com/scikit-learn/scikit-learn/blob/2e481f114169396660f0051eee1bcf6bcddfd556/sklearn/cluster/_kmeans.py#L63-L74 You can also get more details regarding the constraints by looking at the different Estimators validation previously implemented (cf. the `_parameter_constraints` attribute). 
3. All existing simple param validation can now be removed. (simple means that does not depend on the input data or that does not depend on the value of another parameter for instance).
4. Tests that check error messages from simple param validation can also be removed (carefully: we need to keep the tests checking for more complex param validation !).

5. Finally, add the function to the list of the common param validation test https://github.com/scikit-learn/scikit-learn/blob/2e481f114169396660f0051eee1bcf6bcddfd556/sklearn/tests/test_public_functions.py#L11-L13
      and make sure the test passes: `pytest -vl sklearn/tests/test_public_functions.py`

### Functions already updated:

See "details" in section 1 

Be aware that you can see an up-to-date list at the following link: https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/tests/test_public_functions.py#L11


