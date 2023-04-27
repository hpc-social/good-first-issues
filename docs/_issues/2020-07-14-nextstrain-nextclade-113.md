---
tags: help-wanted,tfeat
title: "Strip common prefixes in sequence names"
html_url: "https://github.com/nextstrain/nextclade/issues/113"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

We may save some screen real-estate by removing common prefixes in sequence names (and thus reducing width required by "Sequence width" column, and increasing width of sequence views).


Consider for example sequence names

```
hCoV-19/USA/FL-Miami-06_UMTL-A388/2020
hCoV-19/Madagascar/MA-Antananarivo-01_XXXX-A999/2020
```

We may strip `hCoV-19/`, as it does not bring a lot of valuable information (we only ever do this virus currently) and names would become:

```
USA/FL-Miami-06_UMTL-A388/2020
Madagascar/MA-Antananarivo-01_XXXX-A999/2020
```
Which is significantly shorter. This is also what Nextstrain does, so this would not be something unexpected.

We probably want to stay away from any automatic detection of prefixes, because there isn't a standard for how sequences are named. We may present users with some automatic suggestions though, leaving decision to them.

Prefixes should only be removed upon displaying, no actual data should be modified.
