---
tags: ,enhancement
title: "Download and prepare PFAM-A database"
html_url: "https://github.com/Robaina/Pynteny/issues/71"
user: Robaina
repo: Robaina/Pynteny
---

**Is your feature request related to a problem? Please describe.**
Add support to download the PFAM-A database, besides the PGAP database, to be able to use PFAM models alongside TIGRFAM.

**Describe the solution you'd like**
Add support to download PFAM database, also automatically split original multi-HMM file into separate files (as required by pynteny search). This can be achieved in bash like this:

```bash
#!/bin/bash
# Input hmm file path as a param to this script

csplit --digits=2  --quiet --prefix=hmm $1 "////+1" "{*}"

while read -r id filename
do
    mv "$filename" "$id".hmm
done < <(awk '$1 == "ACC" {print $2,FILENAME; nextfile}' hmm*)
```

But ideally would be integrated in a dedicated python function.

