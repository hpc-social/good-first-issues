---
tags: help-wanted,needs-triage,tbug
title: "Error compiling development instance"
html_url: "https://github.com/nextstrain/nextclade/issues/1140"
user: ArtPoon
repo: nextstrain/nextclade
---

Following recipe in `docs/dev/developed-guide.md`, installation process seems to have gone okay but script threw an exception:
```
    Finished dev [unoptimized + debuginfo] target(s) in 5m 20s
     Running `target/debug/nextclade run data_dev/sequences.fasta --input-dataset=data_dev/ --output-fasta=out/nextclade.aligned.fasta --output-tsv=out/nextclade.tsv --output-tree=out/nextclade.tree.json --in-order --include-reference`
Error: 
   0: --input-dataset: path is invalid. Expected a directory path or a zip archive file path, but got: '"data_dev/"'
```
There is no `data_dev` folder at project root.  I'm on `master` branch, commit c0807f5a1f4c8b44b7e8749b398157df4990ea22
If I point the command to `data/sars-cov-2` instead, another exception is thrown about missing `primers.csv`, which is a deprecated file.  

OS: Ubuntu 20.04.6
cargo 1.67.1