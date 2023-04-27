---
tags: Documentation,Good-first-issue
title: "[Doc]: windows install instructions do not work"
html_url: "https://github.com/matplotlib/matplotlib/issues/24779"
user: tacaswell
repo: matplotlib/matplotlib
---

### Documentation Link

https://matplotlib.org/devdocs/devel/development_setup.html#create-a-dedicated-environment

### Problem

The conda instructions do not work on windows:

 - it is very slow 
 - fails on lxml + pikepdf installation

The venv method does not include in information about how to install all of the dev dependencies

### Suggested improvement

Possible options for conda:
 - find a way to get pikepdf to install on windows
 - remove those entries from environment.yml

Possible solution for venv:
 - document `pip install -r requirements/dev/dev-requirements.txt` 


