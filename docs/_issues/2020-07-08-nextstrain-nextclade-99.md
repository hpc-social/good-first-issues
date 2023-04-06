---
tags: ,help-wanted,priomedium,tfeat
title: "Attach gene map to the bottom-most sequence"
html_url: "https://github.com/nextstrain/nextclade/issues/99"
user: ivan-aksamentov
repo: nextstrain/nextclade
---

Currently the gene map is firmly attached to the bottom of the available table space. This creates a large gap between sequences and gene map when there aren't many sequences.

We want to attach the gene map right after the last sequence in the table, bringing it closer. This should facilitate tracking and comparison.

It might be trickier that usual, because we are using a custom flexbox layout and react-window to manage the table markup and style, especially the positioning. 

There might be a decent javascript solution - the decision where to put gene map is made depending on whether sum of heights of rows is greater than the available height (calculated with already present autosizer wrapper or otherwise). There might also be a CSS solution, using `position: sticky`, or a mixture, using css-in-js (we use styled-components).

Related:

 - #98 Add marker showing current mouse position in sequences and gene map
