---
tags: ,enhancement
title: "report sketch progress from `sketch fromfile`"
html_url: "https://github.com/sourmash-bio/sourmash/issues/2197"
user: bluegenes
repo: sourmash-bio/sourmash
---

When running large databases (e.g. building a new alphabet or ksize for all of gtdb), it would help to have some progress output from `fromfile`, since we have the whole list of signatures we'll build ahead of time.

Current output is informative for each file, but not for building the database as a whole.
```
... reading sequences from genbank/proteomes/GCF_013073765.1_protein.faa.gz
calculated 1 signatures for 4386 sequences in genbank/proteomes/GCF_013073765.1_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_005041175.1_protein.faa.gz
calculated 1 signatures for 4905 sequences in genbank/proteomes/GCF_005041175.1_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_003721835.1_protein.faa.gz
calculated 1 signatures for 4787 sequences in genbank/proteomes/GCF_003721835.1_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_003304895.1_protein.faa.gz
calculated 1 signatures for 4815 sequences in genbank/proteomes/GCF_003304895.1_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_000627885.1_protein.faa.gz
calculated 1 signatures for 4775 sequences in genbank/proteomes/GCF_000627885.1_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_000326325.1_protein.faa.gz
calculated 1 signatures for 4614 sequences in genbank/proteomes/GCF_000326325.1_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_014878905.1_protein.faa.gz
calculated 1 signatures for 4463 sequences in genbank/proteomes/GCF_014878905.1_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_000622655.2_protein.faa.gz
calculated 1 signatures for 5261 sequences in genbank/proteomes/GCF_000622655.2_protein.faa.gz
... reading sequences from genbank/proteomes/GCF_016433285.1_protein.faa.gz
```
I think it'd be useful to hide this output or only output if the user wants verbosity, and instead report build percent.

Just to have some code to start from, merge percent code, [here](https://github.com/sourmash-bio/database-examples/blob/main/mass-merge.py#L111-L113), does a similar thing:

```
if m % 100 == 0:
    merge_percent = float(n)/len(found_idents) * 100
    notify(f"...merging sigs for {merge_name} ({merge_percent:.1f}% of sigs merged)", end="\r")
```