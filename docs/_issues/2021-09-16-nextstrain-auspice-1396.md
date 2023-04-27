---
tags: enhancement
title: "Deactivate filer icon (eye) missing for date range filters"
html_url: "https://github.com/nextstrain/auspice/issues/1396"
user: eharkins
repo: nextstrain/auspice
---

**Current Behavior**  
There is no eye icon allowing the user to deactivate (and reactivate) the filter for date range filters.

**Expected behavior**  
Unless there is a reason why this feature doesn't make sense with this type of filter, it should have the same button as all other filters to deactivate.

**How to reproduce**  
Can be seen at https://nextstrain.org/ncov/open/global?dmin=2020-08-12

**Possible solution**  
Something to do with the `canMakeInactive` property despite the fact that it seems to be specified unconditionally as true for all filters here: https://github.com/nextstrain/auspice/blob/c0ff4e456f55ff907623b146599b530ca88c80c4/src/components/controls/filter.js#L145

**Your environment: if browsing Nextstrain online**  
 - Operating system:  MacOS, also observed in Windows
 - Browser:  Chrome, also observed in Edge
