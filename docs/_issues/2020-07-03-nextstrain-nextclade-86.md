---
tags: help-wanted,tfeat
title: "Link mutations to nextstrain.org"
html_url: "https://github.com/nextstrain/nextclade/issues/86"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

We want to add clickable links into mutation tooltips. These links would lead to the corresponding mutation view in nextstrain.org/ncov colored by the mutated nucleotide.

For example, the mutations at position 11083 would have a link that leads to this URL:

```
https://nextstrain.org/ncov/global?c=gt-nuc_11083
```

![Tooltip](https://user-images.githubusercontent.com/9403403/86481123-ab2adb00-bd4f-11ea-9c54-4039d8b5230a.png)

This is a great way to integrate the tool with nextstrain.org and will hopefully help to grow the ecosystem further.


This would require tooltips or any other informational widgets containing the link to persist, so that the link can be clicked #83 #84 #85 
