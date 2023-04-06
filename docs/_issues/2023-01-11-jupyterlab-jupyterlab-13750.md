---
tags: ,enhancement,help-wanted
title: "List all plugins within JupyterLab"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/13750"
user: fcollonval
repo: jupyterlab/jupyterlab
---

<!-- Welcome! Thank you for contributing. These HTML comments will not render in the issue, but you can delete them once you've read them if you prefer! -->

<!--
Thanks for thinking of a way to improve JupyterLab. If this solves a problem for you, then it probably solves that problem for lots of people! So the whole community will benefit from this request.


Before creating a new feature request please search the issues for relevant feature requests.
-->

### Problem

<!-- Provide a clear and concise description of what problem this feature will solve. For example:

* I'm always frustrated when [...] because [...]
* I would like it if [...] happened when I [...] because [...]
-->

It is possible to enable/disable plugins from the command line. But it is hard to find the plugin names - especially because the name does not have to follow some convention; especially true for third-party extensions.

### Proposed Solution

<!-- Provide a clear and concise description of a way to accomplish what you want. For example:

* Add an option so that when [...]  [...] will happen
 -->

It will be nice to add a new widget listing all plugins (and their description - as this is now [available](https://github.com/jupyterlab/lumino/pull/419) in Lumino). The widget could for example be displayed from the help menu.

The code could get inspiration from https://github.com/jupyterlab-contrib/jupyterlab-plugin-graph - but we should not import the graph feature; or at the expense of using for example d3 that is already a dependency rather than the huge [cytoscape](https://www.npmjs.com/package/cytoscape) package.

### Additional context

<!-- Add any other context or screenshots about the feature request here. You can also include links to examples of other programs that have something similar to your request. For example:

* Another project [...] solved this by [...]
-->
