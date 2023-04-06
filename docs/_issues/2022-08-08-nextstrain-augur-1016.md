---
tags: ,easy-problem,enhancement
title: "Replace custom deepdiff wrapper scripts with deepdiff CLI"
html_url: "https://github.com/nextstrain/augur/issues/1016"
user: huddlej
repo: nextstrain/augur
---

## Context

Augur's functional tests rely on a lightweight wrapper script around DeepDiff, `scripts/diff_jsons.py`, to support comparisons between JSONs. [Augur's dev requirements specify DeepDiff >=4.3.2](https://github.com/nextstrain/augur/blob/67027a6ae6a7a324c8eb646593cc5c0a89650ccf/setup.py#L72).

However, [version 5.2.0 of DeepDiff introduced a command line interface](https://zepworks.com/deepdiff/current/commandline.html) that provides the same functionality (and much more!) than the simple wrapper script.

## Description

We should consider pinning our minimum DeepDiff version at `5.2.0[cli]`, replacing all uses of `diff_jsons.py` with the equivalent `deep diff` command, and removing the `diff_jsons.py` script. The CLI also supports comparisons of other file types like CSV (with the installation of additional Python libraries) which might generally improve our functional tests.

## Examples

```
# Original command.
python3 scripts/diff_jsons.py --significant-digits 4 expected.json observed.json

# With the DeepDiff CLI.
deep diff --significant-digits 4 expected.json observed.json
```

