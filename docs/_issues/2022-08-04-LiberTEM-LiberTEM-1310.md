---
tags: GUI,UX/DX
title: "Outlier filter for live plots"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/1310"
user: uellue
repo: LiberTEM/LiberTEM
---

DECTRIS detectors set "bad" pixels to the maximum possible value. That throws off live plots and is annoying in practice.

We should cut these outliers from the live plot auto ranging.

See for example https://stackoverflow.com/questions/11882393/matplotlib-disregard-outliers-when-plotting