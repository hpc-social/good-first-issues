---
tags: ,Good-First-Issue,help-needed,issue,math-and-logic
title: "[Feature] [Experimental Variogram] Variance should be calculated ALWAYS when experimental variogram is created"
html_url: "https://github.com/DataverseLabs/pyinterpolate/issues/379"
user: SimonMolinsky
repo: DataverseLabs/pyinterpolate
---

**Is your feature request related to a problem? Please describe.**
The `ExperimentalVariogram` class allows the user to choose if **variance** should be calculated. The problem is that variance is needed for multiple modeling tasks, especially to assign the **sill** in the search for the optimal theoretical variogram model.

**Describe the solution you'd like**
Remove the `is_variance` parameter from the `ExperimentalVariogram` class, the `__c_var` attribute, and all related parameters in functions and classes depended on `ExperimentalVariogram`, force algorithm to calculate variance (always). Perform tests to check if everything works fine after this change.
