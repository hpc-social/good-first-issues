---
tags: help-wanted,package-nextclade_web,tfeat
title: "Investigate slow navigation of the tree page"
html_url: "https://github.com/nextstrain/nextclade/issues/440"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

The tree page containing phylogenetic tree rendered by Auspice takes a couple of seconds to navigate to.

In Nextstrain, it does not seem to be the case, even if a much bigger tree is rendered there, plus other widgets:
https://nextstrain.org/ncov/global
Or maybe the pause is hidden behind the loader spinner?

We need to investigate the reason of slowdown and try to make navigation faster. If not, then at least mask it with the loading spinner too.
