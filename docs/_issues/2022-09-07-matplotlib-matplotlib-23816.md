---
tags: Difficulty-Medium,GUI-Qt,Good-first-issue
title: "[ENH]: support PySide6's `snake_case`"
html_url: "https://github.com/matplotlib/matplotlib/issues/23816"
user: bersbersbers
repo: matplotlib/matplotlib
---

### Problem

I use `PySide6` with `snake_case`:
https://doc.qt.io/qtforpython/feature-why.html#the-snake-case-feature

When debugging code in VS Code, I often get this:
> AttributeError: type object 'PySide6.QtWidgets.QFileDialog' has no attribute 'getSaveFileName'


### Proposed solution

In https://github.com/matplotlib/matplotlib/blob/0371cf971ff5c81a963683e3e1c2d48002929e21/lib/matplotlib/backends/qt_compat.py#L100, check if you need to use `QtWidgets.QFileDialog.get_save_file_name`