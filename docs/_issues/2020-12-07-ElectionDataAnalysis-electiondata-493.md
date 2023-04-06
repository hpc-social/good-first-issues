---
tags: 
title: "Explore Alaska census data"
html_url: "https://github.com/ElectionDataAnalysis/electiondata/issues/493"
user: ericmtsai
repo: ElectionDataAnalysis/electiondata
---

This is not technically part of our codebase, but using this as a TODO: we need to explore Alaska's census data and see how (if) it fits into our census data process. The concern is that AK's election districts are broken out at the state-house district level, whereas all the census data occurs at the county level. If the census API provides this specific level of detail, then it should fit in correctly with no changes; otherwise we need to explore how to make it work.