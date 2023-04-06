---
tags: ,New-metric,enhancement
title: "Add METEOR metric"
html_url: "https://github.com/Lightning-AI/torchmetrics/issues/595"
user: stancld
repo: PyTorchLightning/metrics
---

## 🚀 Feature

Add another NLP metric - **METEOR** ([Lavie and Agarval, 2007](https://www.cs.cmu.edu/~alavie/METEOR/pdf/Lavie-Agarwal-2007-METEOR.pdf)).

### Motivation

METEOR is another metric used for the machine translation evaluation similarly to BLEU, however, it demonstrates a higher correlation with human judgements of translation quality.

### Pitch

To support the METEOR metric will be likely to require `nltk` dependency. The `nltk` package is also, however, needed for the ROUGE metric. METEOR thus should not bring any new dependency.

### Additional context

I will be happy to start working on this feature next week if desired to be added :)
