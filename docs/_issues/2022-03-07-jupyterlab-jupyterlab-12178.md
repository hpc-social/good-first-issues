---
tags: ,bug,pkgapputils
title: "Output font size not changing for code cells"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/12178"
user: mpauper
repo: jupyterlab/jupyterlab
---

**Version: 3.3.0**

Hello,

It seems that this has already been implemented but I can't get it to work for output  of code cells. My theme settings are:

```json
{
    "overrides": {
        "code-font-family": "JetBrains Mono",
        "ui-font-size1": "14px",
        "content-font-size1": "18px",
        "content-font-family": "Noto Sans"
    },
    "theme": "JupyterLab Dark",
}
```
It does affect the output of Markdown cells, but the output of other code cells is still smaller. Am I missing another setting?
