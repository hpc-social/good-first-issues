---
tags: Enhancement-✨
title: "Minimum cell cutoff in sc.pl.dotplot"
html_url: "https://github.com/scverse/scanpy/issues/1829"
user: gokceneraslan
repo: scverse/scanpy
---

<!-- What kind of feature would you like to request? -->
- [x] Additional function parameters / changed functionality / changed defaults?
- [ ] New analysis tool: A simple analysis tool you have been using and are missing in `sc.tools`?
- [ ] New plotting function: A kind of plot you would like to seein `sc.pl`?
- [ ] External tools: Do you know an existing package that should go into `sc.external.*`?
- [ ] Other?

<!-- Please describe your wishes below: -->

Especially when we visualize large datasets with multiple categorical variables (e.g. patient, disease, cell type) using `sc.pl.dotplot`, and we use a sequence in the `groupby` argument (`e.g. sc.pl.dotplot(ad, 'genex', groupby=['individual', 'disease_status', 'cell type'])`), sometimes we end up with too few cells in some rows, in which summary statistics like fraction of nonzero expressors or mean expression are not very robust.

To avoid that, I think it'd be cool to have a minimum observation cutoff in the function, where e.g. `min_cells=5` would show `groupby` combinations with at least 5 cells. Without this option, this sort of filtering becomes an annoying pandas exercise (which some might enjoy but possibly not everyone).
