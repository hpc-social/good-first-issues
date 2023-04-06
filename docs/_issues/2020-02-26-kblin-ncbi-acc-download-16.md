---
tags: ,enhancement,help-wanted
title: "Accession range support?"
html_url: "https://github.com/kblin/ncbi-acc-download/issues/16"
user: peterjc
repo: kblin/ncbi-acc-download
---

For a continuous range of accessions, the following range notation is common both in human readable text like data availablitlity sections in papers, and in NCBI cross-references. Could the tool spot this and expand the range automatically? e.g.

```
$ ncbi-acc-download EF590893-EF590896
```

Internally expand this to:

```
$ ncbi-acc-download EF590893 EF590894 EF590895 EF590896
```

Workaround, handy if you just have a couple of ranges to fetch:

```
for i in {590893..590896}; do ncbi-acc-download EF${i}; done
```

(Updated to fix typo, range was not increasing)