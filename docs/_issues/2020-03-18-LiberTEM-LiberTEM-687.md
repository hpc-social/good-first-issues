---
tags: GUI,enhancement
title: "Improved Export/Download support"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/687"
user: sk1p
repo: LiberTEM/LiberTEM
---

This is a continuation of #665, related to discussion in tickets #46, #168, #328

Now that the basic functionality is there, we can get first feedback from users; then it can be further improved:

- [ ] Support for CSV/Text
- [ ] Support for hspy
- [ ] Support for more formats?
- [ ] Better filenames, maybe including name from the GUI?
- [ ] Support for writing analysis parameters into the exported file, to support reproducing the results
- [ ] Find out: can other programs properly open multi-page TIFF documents? DM, HyperSpy, anything else?

## Known issues

- [ ] Image formats (currently TIFF) don't support complex data
- [ ] Code quality in the GUI according to code climate can be improved, although most of the issues are not new...
- [ ] If an analysis decides that it is a good idea to put channels of different dimensions into a single `AnalysisResultSet`, at least the TIFF writer will crash
- [x] CoM export is broken: #723