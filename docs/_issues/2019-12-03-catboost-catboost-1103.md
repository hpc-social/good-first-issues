---
tags: ,help-wanted
title: "Implement ColumnDescriptionClass"
html_url: "https://github.com/catboost/catboost/issues/1103"
user: Noxoomo
repo: catboost/catboost
---

 This class could be used instead of cd file https://catboost.ai/docs/concepts/input-data_column-descfile.html when creating Pool from filez. The class should have init function, methods load and save, and Pool init method should be able to use object of this class instead of cd file during initialization.