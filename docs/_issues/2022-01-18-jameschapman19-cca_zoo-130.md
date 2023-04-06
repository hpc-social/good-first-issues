---
tags: ,enhancement,help-wanted
title: "Implement reordering function to assess feature significance?"
html_url: "https://github.com/jameschapman19/cca_zoo/issues/130"
user: JohannesWiesner
repo: jameschapman19/cca_zoo
---

In their [paper from 2018](https://www.nature.com/articles/s41467-018-05317-y#Sec9), Xia et a. implemented a method to match canonical variates from resampled data sets to the original data set in order to be able to compute p-values for their canonical weights. 

Page 12 (Methods Section):
> As permutation could induce arbitrary axis rotation, which changes the order of canonical variates, or axis reflection, which causes a sign change for the weights, we matched the canonical variates resulting from permuted data matrices to the ones derived from the original data matrix by comparing the clinical loadings (v) (75. Mišić, B. et al. Network-level structure-function relationships in human
neocortex. Cereb. Cortex 26, 3285–96 (2016).)

Here's the code they implemented to achieve this:
https://github.com/cedricx/sCCA/blob/d5a2f4cb071bddd3f7d805e02ff27828b8494c66/sCCA/code/final/cca_functions.R#L191

Would it make sense to implement this method for `cca-zoo`? I am not even sure if this is a 'good' method having [this issue](https://github.com/jameschapman19/cca_zoo/issues/124) in mind? But if I got it right, it's one thing to assess the overall significance of the canonical variates themselves and another thing to assess the significance of the feature weights on the canonical variates? 