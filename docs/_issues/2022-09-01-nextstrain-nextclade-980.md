---
tags: package-nextalign,package-nextclade,tfeat,ttalk
title: "ENH: Output feature table for use during Genbank submission"
html_url: "https://github.com/nextstrain/nextclade/issues/980"
user: corneliusroemer
repo: nextstrain/nextclade
---

### Background

Charlotte Houldcroft mentioned on [Twitter](https://twitter.com/DrCJ_Houldcroft/status/1564631814924279810?s=20&t=p862aRZpUsD-RvvcmUYEEw) that submissions to Genbank are helped enormously if a feature annotation is provided. 

Without such annotation, submissions are marked "unverified", delayed and more back and forth with curators is required.

Here is the documentation for what feature annotation Genbank likes to have: https://www.ncbi.nlm.nih.gov/genbank/feature_table/

### Feature request

Produce such a such a feature table as an extra output option of Nextclade

### Implementation

We have all the details required to create such a table - or it is easy to add that information by extending what we put in our gff input gene map.

The feature table looks similar to a faster file with `>Feature ID` separating sequences, hence we can output a single file for all sequences submitted.

### Further thoughts

It would be good to discuss this feature with data submitters and folks at NCBI to see whether what we have in mind is actually helpful. 