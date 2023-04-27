---
tags: Difficulty-Easy,Good-first-issue,Maintenance,topic-text/fonts
title: "[MNT]: Switch docs/examples to use Noto Sans CJK instead of WenQuanYi Zen Hei as CJK font"
html_url: "https://github.com/matplotlib/matplotlib/issues/25724"
user: anntzer
repo: matplotlib/matplotlib
---

### Summary

Some examples use WenQuanYi Zen Hei as CJK (chinese/japanese/korean) font, but it is less convenient to install on macos (#16112); other examples already rely on Noto Sans CJK, which is still available on Homebrew, so we could just as well always rely on that font instead.

### Proposed fix

Replace usage of WenQuanYi Zen Hei by Noto Sans CJK in the docs/galleries.