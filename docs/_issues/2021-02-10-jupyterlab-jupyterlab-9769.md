---
tags: enhancement,help-wanted,pkgdocregistry
title: "Check file changes based on content instead of the last_modified metadata"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/9769"
user: skukhtichev
repo: jupyterlab/jupyterlab
---

<!--
Welcome! Thanks for thinking of a way to improve JupyterLab. If this solves a problem for you, then it probably solves that problem for lots of people! So the whole community will benefit from this request.


Before creating a new feature request please search the issues for relevant feature requests.
-->

### Problem
JupyterLab mechanism to detect a file changes is based on last_modified parameter set in the metadata: https://github.com/jupyterlab/jupyterlab/blob/b4db7f03d2ad0b91a9c8c252c56ae5e4a9408fbb/packages/docregistry/src/context.ts#L644-L649. 
If the file last_modified parameter was changed without changing the content then JupyterLab shows the following message
![image (11)](https://user-images.githubusercontent.com/12250108/107552472-dc1b9a00-6bd3-11eb-9c8c-3cf7b274e0c1.png)
The issue happens when sync tools are used that updates files last modified timestamp.


<!-- Provide a clear and concise description of what problem this feature will solve. For example:

* I'm always frustrated when [...] because [...]
* I would like it if [...] happened when I [...] because [...]
-->

### Proposed Solution
Using content based check mechanism (e.g. hash) will prevent showing the dialog when the last modified timestamp changed without changing a file content
<!-- Provide a clear and concise description of a way to accomplish what you want. For example:

* Add an option so that when [...]  [...] will happen
 -->

### Additional context

<!-- Add any other context or screenshots about the feature request here. You can also include links to examples of other programs that have something similar to your request. For example:

* Another project [...] solved this by [...]
-->
