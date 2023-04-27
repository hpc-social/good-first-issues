---
title: "how to specify db-load-mode in precomputed_alignments_mmseqs.py"
html_url: "https://github.com/aqlaboratory/openfold/issues/190"
user: lzhangUT
repo: aqlaboratory/openfold
---

Hi,
I am using the recomputed_alignments_mmseqs.py to search for MSA for my input.fasta which has 9 sequences inside. 
but the mmseq2 is taking too long to run it, it is already over 4 hours, but still hasn't finished.
When I was using colabfold, they do have an argument db_load-mode to specify msa search for a batch. I see you have this parameter in the colabfold_search.py, but I dont know how to specify that in the command of recomputed_alignments_mmseqs.py.
Thank you.
and how should I maximize the usage of cpus for msa search?