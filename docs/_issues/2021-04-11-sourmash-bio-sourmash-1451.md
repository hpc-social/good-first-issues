---
tags: python,testing
title: "write command-line test for `lca summarize --query-from-file`"
html_url: "https://github.com/sourmash-bio/sourmash/issues/1451"
user: ctb
repo: sourmash-bio/sourmash
---

per https://github.com/dib-lab/sourmash/pull/1423/files#r604406992 as well as attached screenshot, we do not currently test `sourmash lca summarize --query-from-file`
<img width="806" alt="Screen Shot 2021-04-11 at 10 57 06 AM" src="https://user-images.githubusercontent.com/51016/114315693-e4e5fa80-9ab4-11eb-85ba-aea2e4e63ce1.png">

To address this issue:
* make a copy of `test_single_summarize()` in `tests/test_lca.py` and name it something like `test_single_summarize_query_from_file()`;
* modify the new test to create a text file containing the path to `input_sig`
* modify the `utils.runscript(...)` command to remove `--query` and instead pass in `--query-from-file` with the new text file