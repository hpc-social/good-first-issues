---
tags: help-wanted
title: "Make meaningfulLabels = FALSE argument work in dag_greta()"
html_url: "https://github.com/flyaflya/causact/issues/9"
user: flyaflya
repo: flyaflya/causact
---

currently, within dag_greta() the following line is automatically added:

`
draws       <- replaceLabels(draws)   #POSTERIOR
`

This line should be omitted when meaningfulLabels = FALSE is passed to dag_greta().