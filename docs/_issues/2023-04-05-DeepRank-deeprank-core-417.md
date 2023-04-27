---
tags: CI,testing
title: "Use pathlib or os.join method and global TEST_PATH variable consistently in test modules"
html_url: "https://github.com/DeepRank/deeprank-core/issues/417"
user: DaniBodor
repo: DeepRank/deeprank-core
---

From [this comment](https://github.com/DeepRank/deeprank-core/pull/387#pullrequestreview-1372515081) (see below for examples):

> We can either:
> 
>     Use forward slashes (/) or commas (,) with pathlib functions - both options work. The Path() object will convert forward slashes or commas into the correct kind of slash for the current operating system (nice blog post about it [here](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f#:~:text=You%20should%20use%20forward%20slashes,operator%20directly%20in%20your%20code.)).
>     Use os.path.join() method.

[Furthermore](https://github.com/DeepRank/deeprank-core/pull/387#issuecomment-1497607201): 
We could adjust the `TEST_PATH` variable to `TESTDATA_PATH` and use 1 fewer folder level in the data, as there is no added benefit of having (nearly) identically named folders to the final file.