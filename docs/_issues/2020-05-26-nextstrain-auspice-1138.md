---
tags: bug,low-priority
title: "Zooming out from a labelled subtree does not correctly update the URL query"
html_url: "https://github.com/nextstrain/auspice/issues/1138"
user: jameshadfield
repo: nextstrain/auspice
---

**Current Behavior**  
Clicking on the root branch of a displayed subtree zooms out (in the tree). If the currently zoomed-to branch has a label set, then this is displayed in the URL query as `?label=...`. When zooming out from this subtree by clicking on the root, the URL query does not update.

**Expected behavior**  
Upon zooming out from the subtree by clicking on the root, then the label should disappear from the URL query.

**How to reproduce**  
Steps to reproduce the current behavior:  
1. Open https://nextstrain.org/staging/test/tree-labels-2020-05-26
2. Click on the branch labelled "string-value" to zoom into the subclade. Observe that the URL query updates.
3. Click on the root branch of the subtree (the left-most bit).
4. We correctly zoom out, however the URL query remains when it should be cleared.

**Possible solution**  
Update the URL (redux) middleware to listen for the appropriate redux action & update the query

Note that pressing "reset layout" when zoomed in does correctly clear the URL query.

**Your environment: if browsing Nextstrain online**  
Auspice 2.15.0

