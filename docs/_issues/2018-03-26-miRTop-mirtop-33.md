---
tags: enhancement,help-wanted
title: "Add stats output to multiqc "
html_url: "https://github.com/miRTop/mirtop/issues/33"
user: lpantano
repo: miRTop/mirtop
---

Add a module for [multiqc tool](https://github.com/ewels/MultiQC#contributions--support) that parses the example [stats file](https://github.com/miRTop/mirtop/blob/dev/data/examples/stats/mirtop_stats.txt) so it can be integrated in multiqc report.

Ideally, we need to add first a commented line like this when creating the stats file:

```
# mirtop stats version X samples: s1, s2 ,s2 ....
```

This can go here: https://github.com/miRTop/mirtop/blob/dev/mirtop/gff/stats.py#L17