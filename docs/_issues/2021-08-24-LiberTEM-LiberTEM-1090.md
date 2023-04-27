---
tags: GUI,UX/DX,notebooks
title: "Possible confusion between current GUI parameters and notebook download"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/1090"
user: uellue
repo: LiberTEM/LiberTEM
---

Not sure how severe this issue is, but listing it here at least for documentation and discussion purposes.

## How to reproduce

* Add an analysis in the GUI with selectors or similar and run it
* Change the parameters/selectors in the GUI without re-running
* "Download" -> copy notebook and inspect the parameters for the analysis

## Observed behavior

The notebook contains the parameters from the last run

## Expected behavior

Not sure if a user would expect the current GUI parameters or the last run. In any case, it is an ambiguous situation.

## Possible solutions

* Warning or other indication of ambiguity/invalid state/requiring re-run, for example different icons or color change of buttons?
* Disable download until run?
* Run upon downloading?
* Ignore and leave as-is?
