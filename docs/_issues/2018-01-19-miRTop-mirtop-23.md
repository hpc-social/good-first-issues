---
tags: ,help-wanted,internal
title: "Function to parse queries and apply to the GFF file"
html_url: "https://github.com/miRTop/mirtop/issues/23"
user: lpantano
repo: miRTop/mirtop
---

The idea is to have an option shared by many functions called `--query`, that allows filtering of the GFF format for:

* `Name`, `Variant`, `Filter`, `type` values of the GFF format. To learn about where they are in the line of the GFF file go to: https://github.com/miRTop/incubator/blob/master/format/definition.md
* It should allow: `==`, `!=`, `~//` (regular expression)
* Allows `and` , `or` operations
The option should be added here: https://github.com/miRTop/mirtop/blob/dev/mirtop/libs/parse.py. Probably under the function `counts` (it would be there soon)

And the function that parse the query value should be here: https://github.com/miRTop/mirtop/blob/dev/mirtop/gff/query.py

The idea should be something like this:

`mirtop counts -i GFF -o OUTFOLDER --query "Filter == PASS and Name~/let-7/"`

That should get the GFF file, apply the query filters, and then do whatever `counts` function makes.

This issue can be resolved with a **single function** that work with the `--query` value and a line of the **GFF** file, given TRUE or FALSE, depending on the query.

Test unit should be implemented at https://github.com/miRTop/mirtop/blob/dev/test/test_functions.py