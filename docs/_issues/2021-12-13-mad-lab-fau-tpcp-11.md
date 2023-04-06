---
tags: help-wanted
title: "Representations for objects"
html_url: "https://github.com/mad-lab-fau/tpcp/issues/11"
user: AKuederle
repo: mad-lab-fau/tpcp
---

#13 implements a basic version of a representation.

However, it has some remaining issues:

- [ ] Long representations are alls hown in the same line (maybe use this: https://github.com/scikit-learn/scikit-learn/blob/056f993b411c1fa5cf6a2ced8e51de03617b25b4/sklearn/base.py#L104)
- [ ] objects with unuasual representaitons (e.g. pd.DataFrames) can mess up the formatting, when included as a paramter)

Some further notes:

- sklearn does something very elegant and does not include parameters in the repr that are still at their default value.
- Dataset already has a repr that does not include the parameters. It might be nice to include the custom user parameters in that representation as well.