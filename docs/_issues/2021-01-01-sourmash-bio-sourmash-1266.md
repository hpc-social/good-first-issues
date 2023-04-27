---
tags: good-next-issue
title: "add more hash manipulation utilities to sourmash CLI"
html_url: "https://github.com/sourmash-bio/sourmash/issues/1266"
user: ctb
repo: sourmash-bio/sourmash
---

yesterday, I spent some time digging into a sourmash use case with @shannonekj, and a few different reasonably generic utility script needs emerged.

the code for this is [in a private repository](https://github.com/ctb/2020-shannon-fish-sex/blob/latest/compare-abund.ipynb) so I'll try to describe things here - we were looking for differential presence of hashes in a genome between two samples (specifically, looking for hashes that correlated with male vs female genomes).

to do this, we needed the following new functionality -

* code to export hashes, together with their abundances, from a signature computed with track-abund; viz #1098 
* code to intersect one track-abund signature with another signature, without flattening the abundances in the first signature. (note that `sourmash sig intersect` flattens all signatures) - this could be maybe be done by updating `sourmash sig intersect`
* code to select sequences in a FASTA/FASTQ file that have some number of overlapping hashes with a signature (this has been a repeatedly useful utility that I've implemented a dozen times in various contexts 😆 )
* code to estimate the abundance of sequences based on median hash abundance from a signature (i.e. estimate sequence abundance in a FASTA/FASTQ file using abundances from a track-abund sourmash signature) - this may be too niche to implement in sourmash directly, but I feel like it has come in handy.

I implemented all of this in a Jupyter notebook fairly easily, but it'd nice to have this in the sourmash CLI.

since code exists for all of this and I can make it available upon request, I'll label this as a good first issue...

