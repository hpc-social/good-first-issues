---
tags: ,docs,follow-up
title: "Add documentation on cli commands (including piping)"
html_url: "https://github.com/scikit-hep/pyhf/issues/212"
user: kratsg
repo: scikit-hep/pyhf
---

# Description

> cat recast.json|pyhf cls workspace.json --patch -
> cat recast.json|pyhf cls <(curl -s http://physics.nyu.edu/~lh1132/workspace.json) --patch -

These need to get added to documentation somewhere. 

# Relevant Issues and Pull Requests

#204 introduced some of these commands for us; #205 implemented the new `cls` command. #197 introduced the `xml2json` command.