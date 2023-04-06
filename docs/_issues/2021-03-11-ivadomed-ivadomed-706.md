---
tags: ,cardDESIGN_DISCUSSION,documentation,help-wanted
title: "Keep only typical config files + Standardise them"
html_url: "https://github.com/ivadomed/ivadomed/issues/706"
user: charleygros
repo: ivadomed/ivadomed
---

We currently have 10+ config files.

At the start of the `ivadomed` project, we were dumping our config files there to share them among students running the same experiment.

We should clean this folder, remove the ones that are too specific and standardize them (e.g. use open source datasets instead of `sct_testing/large`).

Ideally, we will have only one config file per application, eg classification, segmentation_single_class, segmentation_multi_class, segmentation_film etc. AND refer to them in the documentation.

For config files that are specific to a certain experiment, a GH repository can be created to host them, see [example](https://github.com/ivadomed/article-softseg).

Notes:
- `contrast_dct.json` can be removed or moved to `dev`.