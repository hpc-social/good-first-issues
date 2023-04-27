---
tags: help-wanted,tfeat
title: "Mark \"short\" sequences"
html_url: "https://github.com/nextstrain/nextclade/issues/519"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

We can never be sure whether sequences with long contiguous missing fragments are what user intends to analyze or whether it is a sequencing issue that needs to be reported.

For these sequences mutations are not called for missing regions and often genes are not translated due to nucleotides simply missing for the most part. Clade assignment can also be unreliable.

In these cases we might mark the suspicious samples with some sort of a marker in the UI and perhaps to add a property to the file outputs.

This would be an informational severity flag, and not a warning, because for some users this might be what they meant to do.
