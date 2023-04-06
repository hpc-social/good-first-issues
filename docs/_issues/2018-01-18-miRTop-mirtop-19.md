---
tags: ,enhancement,help-wanted
title: "support ggplot style figures for stats command"
html_url: "https://github.com/miRTop/mirtop/issues/19"
user: lpantano
repo: miRTop/mirtop
---

Generate a plot like this:

 ![](https://github.com/miRTop/mirtop/raw/dev/data/examples/plot/example_count.png)

from a file that looks like this:

https://github.com/miRTop/mirtop/blob/master/data/examples/plot/example_count.tsv

Libraries to use:
* https://seaborn.pydata.org/examples/color_palettes.html
* https://github.com/yhat/ggpy

The code can be added as a script under `scripts` folder where a function get a file with a similar content that the previous one. The function should generate a similar figure than the example.

After a function like that is implemented, the next step is to integrate in command line:

A new option in `stats`  subcommand like `--plot` should generate a plot showing the difference between GFF files. 

For instance, in this example:
```
cd mirtop/data
mirtop stats -o test_out example/gff/correct_file.gff
```

if we add `--plot` it should output the previous figure. 

For that, it has to be implemented code at https://github.com/miRTop/mirtop/blob/dev/mirtop/gff/stats.py#L29. 

The output of that function contains *_count and *_sum category.  There should be a plot for each of that.

