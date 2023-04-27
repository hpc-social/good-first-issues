---
title: "Code duplication within eval functionality & unittests"
html_url: "https://github.com/zdelrosario/py_grama/issues/199"
user: mstites
repo: zdelrosario/py_grama
---

Throughout grama, there is currently a lot of redudent code that could be combined into common functionality. De-duplicated code would improve readability and maintainability. 

From my work so far, I have identified two major areas to start work on code de-duplication within eval verbs:

1. Unittesting eval verbs: both test_evals.py and test_evals.py have a lot of repeating code. For example, test_lhs and test_sample follow almost identical tests, except for the specific df arg and kwargs. _These tests could be combined into a helper function that takes a specific df arg (for input and for testing against(?)) and passes kwargs. I created the class TestEvalInvariants which groups invariaant unittests for eval verbs*. Similar code/classes could be developed for other tests._
2. Eval verbs invariant testing: PR #195 combined invariant tests into a centralized helper function. However, this invariant testing currently is performed twice for any eval_* verb that calls eval_df as part of its operation (e.g. eval_nominal, eval_conservative). This is necessary with the way the code is currently written, as invariants must be tested before any operation is done on the model or dataframe objects (these eval_* verbs plus eval_df are all user accessible functions). _A potential way to remove this code duplication would be to create a helper function that performs the necessary part of eval_df these functions require, so that these functions can call an internal helper function (w/o invariant tests) instead of eval_df._

Other areas of the code also need work in deduplication, and other issues should be opened (or this one modified) to cover those. A good place to start would just be working on de-duplication throughout the test suite.

_*This class is a good start, however, there is quite a bit of code duplication here between the df_arg and df_arg_2 functions. These could also be combined to reduce code duplication._