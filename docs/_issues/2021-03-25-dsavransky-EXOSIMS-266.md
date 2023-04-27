---
tags: enhancement
title: "Linear Scheduler Coefficients should be Named quantities in the JSON input"
html_url: "https://github.com/dsavransky/EXOSIMS/issues/266"
user: dsavransky
repo: dsavransky/EXOSIMS
---

**Is your feature request related to a problem? Please describe.**
Right now, all coefficients are entered as arrays where the ordering is implicit and has to match the code.  Different schedulers also have different ordering, making JSON input potentially ambiguous and unportable.  Furthermore, when coefficients are added/moved around in the code, JSON scripts grow stale.

**Describe the solution you'd like**
All coefficients should be individual named quantities in the input scripts. 
