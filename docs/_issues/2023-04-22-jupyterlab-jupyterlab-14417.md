---
tags: enhancement,pkgdocumentsearch
title: "Expose search shortcuts in button tooltips"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/14417"
user: krassowski
repo: jupyterlab/jupyterlab
---

### Problem

Buttons next/previous buttons in search box have shortcuts <kbd>Ctrl</kbd> + <kbd>G</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> but those are not shown anywhere which means users don't know about them.

### Proposed Solution

Show shortcuts in tooltips.

![Screenshot from 2023-04-22 15-59-40](https://user-images.githubusercontent.com/5832902/233792075-01d489a5-978d-456f-af7c-9b01351410ab.png)
![Screenshot from 2023-04-22 15-59-43](https://user-images.githubusercontent.com/5832902/233792077-ce46c93b-5e40-459d-8668-2f7952537f50.png)

The tooltips are defined in:

https://github.com/jupyterlab/jupyterlab/blob/a9201ff63421c308733a01be1e61c16da0093bd1/packages/documentsearch/src/searchview.tsx#L276-L292

and the shortcuts are defined here:

https://github.com/jupyterlab/jupyterlab/blob/a9201ff63421c308733a01be1e61c16da0093bd1/packages/documentsearch-extension/schema/plugin.json#L41-L51

One would need to extract the keybindings from the shortcuts (see below) and add them the tooltip.

### Additional context

This is what other IDEs do. We also do this for debugger buttons, e.g.:

![Screenshot from 2023-04-22 16-00-09](https://user-images.githubusercontent.com/5832902/233792087-471068b6-a0cc-4a0f-85b9-a1b512b66d02.png)

The debugger buttons are implemented with `CommandToolbarButtonComponent`/`ToolbarButtonComponent` which uses `propsFromCommand`:

https://github.com/jupyterlab/jupyterlab/blob/a9201ff63421c308733a01be1e61c16da0093bd1/packages/ui-components/src/components/toolbar.tsx#L848

which retrieves and formats shortcut from the command:

https://github.com/jupyterlab/jupyterlab/blob/a9201ff63421c308733a01be1e61c16da0093bd1/packages/ui-components/src/components/toolbar.tsx#L1074-L1081