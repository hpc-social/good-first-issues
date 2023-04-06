---
tags: ,help-wanted
title: "Add overflow values to the tests"
html_url: "https://github.com/simd-everywhere/simde/issues/688"
user: mr-c
repo: simd-everywhere/simde
---

Examples from https://github.com/simd-everywhere/simde/pull/685

``` 
SIMDE_FLOAT32_C(-2147483650.0)
SIMDE_FLOAT32_C( 2147483649.0)

SIMDE_FLOAT64_C(-2147483650.0)
SIMDE_FLOAT64_C( 2147483649.0)
```

The procedure is:
1. Find tests that use `SIMDE_FLOAT32_C` or `SIMDE_FLOAT64_C` in their `test_vec`
2. Copy-n-paste an entry in the `test_vec`, modifying the inputs using the overflow values above. Don't worry about changing the expected result (`r`) yet.
3. Run the tests on a processor that supports the native intrinsic. Copy the correct output values from the error logs.
4. Send a PR
5. Repeat!