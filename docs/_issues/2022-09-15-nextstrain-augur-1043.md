---
tags: easy-problem,enhancement,please-take-this-issue
title: "Add support for masking gap characters"
html_url: "https://github.com/nextstrain/augur/issues/1043"
user: huddlej
repo: nextstrain/augur
---

### Context
We occasionally pass sequences to augur ancestral (or other downstream tools) that include gap characters (`-`) that should actually be missing base characters (`N`). Since "augur ancestral --infer-ambiguous" doesn't actually infer states at gap characters and instead only works on N characters, the resulting output can be surprising/confusing.

### Description
One solution to the problem would be to allow users to mask gap characters with `augur mask` through a new argument like `--mask-gaps`. The closest equivalent of this functionality is the `--mask-invalid` flag, but we consider `-` to be a valid nucleotide character and would need to treat these as a special case.

### Examples
```
augur mask --sequences aligned.fasta --mask-gaps --output masked.fasta
```