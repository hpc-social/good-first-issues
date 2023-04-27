---
tags: Enhancement-✨
title: "PAGA connectivity score"
html_url: "https://github.com/scverse/scanpy/issues/1133"
user: rsggsr
repo: scverse/scanpy
---

Hi

I am recently transformed Seurat object to scanpy and use it for further pseudotime analysis (PAGA) and it performs really well. 

But I have three question here:

1) I am wondering if anybody here knows how to make PAGA connectivity score heatmap (ref: Popescu et al, 2019, Nature) which shows connections strength between partitions. I've tried dendrogram in scanpy (pl.coorelation.matrix) but we'd like to try more. 

2) And also if anyone knows if we could perform differential expression on the partitions by PAGA to find the marker gene along the potential path?

3) PAGA generated a pie chart in every partition But does anyone know whether I could acquire the real percentage of the pie representing different Seurat cluster I input?

Thanks in advance for everyone's help!