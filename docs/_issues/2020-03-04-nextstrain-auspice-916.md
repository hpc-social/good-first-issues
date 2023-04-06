---
tags: ,please-take-this-issue
title: "Sidebar toggle to show labels for all tips in tree"
html_url: "https://github.com/nextstrain/auspice/issues/916"
user: jameshadfield
repo: nextstrain/auspice
---

### Background:

Currently we only display tip labels when the total number of tips in-view is below a certain threshold. This prevents hundreds of tips being displayed on big trees, and allows small trees, or zoomed in sections of trees, to display labels.

(Potentially see #237 for further information)

### This issue

There should be a toggle in the sidebar (such as we have for "Show Confidence Intervals") which results in tips being displayed for all visible nodes. It's initial state should be defined by the threshold discussed above. 
