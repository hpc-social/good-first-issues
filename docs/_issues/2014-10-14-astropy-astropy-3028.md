---
tags: ,Effort-low,Feature-Request,Package-novice,modeling
title: "Allow tuples/iterables as convenience for setting contraints on model parameters"
html_url: "https://github.com/astropy/astropy/issues/3028"
user: embray
repo: astropy/astropy
---

Currently it is possible to specify constraints on parameters when instantiating a model by providing keyword arguments named after the constraints, and dict that provides settings to that constraint for some (or all) parameters.  For example:

`m = SomeModel(1, 2, 3, fixed={'param_a': True, 'param_b': False})`

The dict-based assignment is definitely nice and explicit, and also good if you only need to specify some constraint on a few parameters.  But as @mhvk suggested it would also be convenient to accept a sequence that provides that constraint for all parameters.  For example if the parameters on a model are 'param_a', 'param_b', and 'param_c' one could write:

`m = SomeModel(1, 2, 3, fixed=(True, False, True))`

instead of

`m = SomeModel(1, 2, 3, fixed={'param_a': True, 'param_b': False, 'param_c': True})`

This would work since by design the parameters on each model have a standard "order" associated with them.  I see no harm in allowing both styles.
