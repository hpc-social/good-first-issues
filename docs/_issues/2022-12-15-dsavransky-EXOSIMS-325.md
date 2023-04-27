---
title: "target completeness should be cached"
html_url: "https://github.com/dsavransky/EXOSIMS/issues/325"
user: dsavransky
repo: dsavransky/EXOSIMS
---

**Is your feature request related to a problem? Please describe.**
When using ``GarrettCompleteness``, the target completeness calculation takes several minutes for large target lists for every sim object built.  This should be cached like the other values.  Should be implemented in method ``target_cmopleteness``.  Probably not needed for BrownCompleteness but could be added there as well. 


