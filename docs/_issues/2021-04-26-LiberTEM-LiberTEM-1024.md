---
tags: GUI,UX/DX,enhancement
title: "Allow users to access the PNGs from the web GUI"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/1024"
user: uellue
repo: LiberTEM/LiberTEM
---

It would be nice if one could copy, drag&drop or download the PNG images from the web GUI. That would close a gap between binary results download, notebook download and screenshots. 

Right now the PNGs are internal "blobs" in an SVG, which don't allow any of these interactions. Since LiberTEM now saves the state of an analysis and can therefore regenerate a PNG as needed, for example when reloading, one could perhaps simply include a link somewhere in the analysis that opens the PNG in a new tab?