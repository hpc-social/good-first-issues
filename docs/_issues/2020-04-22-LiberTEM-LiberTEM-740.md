---
tags: GUI,UX/DX
title: "GUI: Selector handle behavior"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/740"
user: uellue
repo: LiberTEM/LiberTEM
---

The selectors in the GUI behave oddly in some instances:

## Drag and drop

Observed behavior: Quickly dragging outside the host panel drops the selector at some random position on the way. One has to click and drag it again to move it again. This behavior makes it difficult to move handles right to the border of the panel: They are always dropped a bit before. They can only be moved to the borders by keyboard.

Expected behavior: The selector is moved up to the boundary of the panel and remains dragging, i.e. is not dropped. It can be moved up to the border by mouse.

## Keyboard interaction

Observed behavior: The selector handles for rectangular ROI can be moved out of the field of view by keyboard. They are then out of reach for mouse interaction.

Expected behavior: The selector handles behave like the center selector for Disk ROI, i.e. can be moved only to the corners by keyboard and mouse.

As a side note, it happens with the "Choose specimen region" of Region clustering analysis in the same way.

## FFT analysis leftmost panel

Observed behavior: Both handles can be moved out of the panel by keyboard. They can't be moved back after they lost focus.

Expected behavior: They can be brought back or they can't be moved outside.

## FFT analysis central panel

Moving the selectors feels more sluggish than with the other analyses.