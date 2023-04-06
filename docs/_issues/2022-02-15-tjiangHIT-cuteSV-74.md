---
title: "Missing SVs"
html_url: "https://github.com/tjiangHIT/cuteSV/issues/74"
user: bnoyvert
repo: tjiangHIT/cuteSV
---

Hi @tjiangHIT ,

I am sorry, I encountered another problem. The attached bam file example has a clear heterozygous 97 base insertion at `1:1501010`.
![IGV_undetected](https://user-images.githubusercontent.com/97630376/154115648-e43cf69e-9c46-4e26-b2a5-d9c8cd5eecbd.png)
CuteSV doesn't detect it. Even the signature files are empty.
The command used is 
`cuteSV --genotype undetected.bam human_g1k_v37.fasta undetected.vcf  undetected --retain_work_dir`
Note that the reference file used here is the standard hg19 fasta file, but the original bam file was created using an extended hg19 reference, containing a few additional "chromosomes". (Unfortunately I don't have this fasta file, but chromosome 1 sequence should be exactly the same.) I suspect this might be the cause of the problem, but cuteSV doesn't show any errors or warnings.

It is also interesting that if one cuts a more narrow slice of the bam file containing only the reads covering the insertion, then cuteSV does detect the insertion!

This is not the only example. I have seen many missing deletions and insertions when called from the original whole genome bam file.

Thank you for your help!
Boris

[undetected.zip](https://github.com/tjiangHIT/cuteSV/files/8073511/undetected.zip)