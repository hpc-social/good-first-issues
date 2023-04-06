---
tags: ,enhancement,help-wanted,shiny
title: "Make nicer display of non edit view of document"
html_url: "https://github.com/ropenscilabs/qcoder/issues/35"
user: elinw
repo: ropenscilabs/qcoder
---

Right now we are using verbatim text and it's pretty ugly and unreadable.  Switch to use html (will mean adding at least  `<p></p>` tags  and also consider converting QCODE tags to `<mark></mark>`.   This is ideally a gsub use case I would think.