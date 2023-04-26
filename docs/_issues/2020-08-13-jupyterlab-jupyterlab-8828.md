---
tags: maintenance,tagExamples
title: "Update `examples` folder to include localization."
html_url: "https://github.com/jupyterlab/jupyterlab/issues/8828"
user: goanpeca
repo: jupyterlab/jupyterlab
---

### Task

After the localization work, the examples folder kept working as expected but the code does not make active use of localization.

In order to promote localizable code, it would be great to be able to showcase the bundled examples following the translation pattern.

### Proposed Solution

Update the code in the [examples folder](https://github.com/jupyterlab/jupyterlab/tree/master/examples) to use an actual `ITranslator` (instead of the `nullTranslator` that is provided under the hood, and does nothing)

### Additional context

Ping me for questions!