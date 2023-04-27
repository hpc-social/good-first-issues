---
tags: GUI,UX/DX,enhancement
title: "Path input for file browser should be able to open a file directly"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/969"
user: uellue
repo: LiberTEM/LiberTEM
---

## How to reproduce

Enter the full path to a file into the path input field of the file browser.

## What happens

The GUI shows a "not found" error.

```
distributed.worker - WARNING -  Compute Failed
Function:  get_fs_listing
args:      ()
kwargs:    {}
Exception: FSError('path E:\\LargeData\\LargeData\\ER-C-1\\groups\\data_science\\data\\reference\\MIB\\20200518 165148/default.hdr could not be found', 'NOT_FOUND', 'E:\\LargeData\\LargeData\\ER-C-1\\groups\\data_science\\data\\reference\\MIB\\20200518 165148')
```

## What should happen

The file is opened.

## Workaround

Just enter the folder and click on the file.