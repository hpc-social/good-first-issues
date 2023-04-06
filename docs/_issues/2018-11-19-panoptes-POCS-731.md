---
tags: ,bug
title: "Target Field names cannot be all numbers"
html_url: "https://github.com/panoptes/POCS/issues/731"
user: wtgee
repo: panoptes/POCS
---

There is a bug in the reading of the targets file such that if the name is all numbers it will try to parse as an integer and fail. The result is only to skip the one individual target.

Not sure we *need* to fix this but wanted to make an issue to be aware. 