---
tags: ,feature
title: "Calculate the area under the balanced precision-recall curve (AUBPRC)"
html_url: "https://github.com/SchlossLab/mikropml/issues/330"
user: kelly-sovacool
repo: SchlossLab/mikropml
---

The area under the precision recall-curve (AUPRC) changes depending on the frequency of labelled positives in the dataset. Therefore, AUPRC cannot be directly compared between models trained on datasets with different frequencies of positives. This is unlike AUROC, where 0.5 is always the baseline for binary classification representing a random classifier. 

To solve this problem, Wu _et al._ ([10.1016/j.ajhg.2021.08.012](https://doi.org/10.1016/j.ajhg.2021.08.012)) developed the concepts of balanced precision and area under the balanced precision-recall curve (AUBPRC). Balanced precision is the precision that would have been expected if the frequency of positives were balanced at 50% (Equation 1). AUBPRC can be calculated directly from the AUPRC (Equation 7).

Let's incorporate Equations 1 and 7 as functions.