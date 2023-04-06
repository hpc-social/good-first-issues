---
tags: ,Good-First-Issue,documentation
title: "Improve basic usage tutorial by mentioning limited support for \"--latest\" / \"-l\""
html_url: "https://github.com/containers/podman/issues/17019"
user: biergit
repo: containers/podman
---

The commands in the [basic usage tutorial](https://github.com/containers/podman/blob/main/docs/tutorials/podman_tutorial.md) do not work for Windows and probably neither for Mac (see ["--latest"](https://docs.podman.io/en/latest/markdown/podman-inspect.1.html#latest-l) documentation).
I would suggest to either mention the current limitation around using the "--latest" flag or go with something that works in all environments to improve the first impression when picking up Podman.