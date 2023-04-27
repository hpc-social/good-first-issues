---
tags: Low-priority,help-wanted,idl/gdl-only
title: "test_resolve_routine fails (first of all, it fails with IDL)"
html_url: "https://github.com/gnudatalanguage/gdl/issues/146"
user: opoplawski
repo: gnudatalanguage/gdl
---

```
161: Test command: /export/home/orion/fedora/gdl/gdl-0.9.8/build/testsuite/launchtest "test_resolve_routine.pro"
161: Test timeout computed to be: 9.99988e+06
161: % Compiled module: TEST_RESOLVE_ROUTINE.
161: % TEST_ALL_TEST_ROUTINES: No files <<test_*pro>> in current directory (/export/home/orion/fedora/gdl/gdl-0.9.8/build/testsuite)
161: % Compiled module: ERRORS_CUMUL.
161: % Compiled module: BANNER_FOR_TESTSUITE.
161: % Compiled module: GDL_IDL_FL.
161: % TEST_RESOLVE_ROUTINE: 
161: ============================================================
161: % TEST_RESOLVE_ROUTINE: 
161: =                                                          =
161: % TEST_RESOLVE_ROUTINE: 
161: =  1 errors encountered during TEST_RESOLVE_ROUTINE tests  =
161: % TEST_RESOLVE_ROUTINE: 
161: =                                                          =
161: % TEST_RESOLVE_ROUTINE: 
161: ============================================================
161/194 Test #161: test_resolve_routine.pro ...........***Failed    0.22 sec
```

Perhaps an issue with out of tree builds?