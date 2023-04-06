---
tags: ,bug
title: "Error is thrown when Dialog has no buttons"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/11897"
user: mnowacki-b
repo: jupyterlab/jupyterlab
---

<!-- Welcome! Thank you for contributing. These HTML comments will not render in the issue.

Before creating a new issue:
* Search for relevant issues
* Follow the issue reporting guidelines:
https://jupyterlab.readthedocs.io/en/latest/getting_started/issue.html
-->

## Description
Seems there are insufficient checks being performed in `apputils` Dialog class. When a dialog with no buttons is created it results in an error. The dialog is still visible but in the console you can see an error log.

## Reproduce
<!--Describe step-by-step instructions to reproduce the behavior-->

1. Create a new dialog without any buttons:
```ts
import {]
  Dialog
} from '@jupyterlab/apputils';

const dialog = new Dialog({
    title: 'title',
    body: createPreformattedTextWidget('body'),
    buttons: [],
    hasClose: false,
  });
```
2. launch the dialog:
```ts
dialog.launch()
```
3. Observe the console log:
error:
```
TypeError: Cannot read properties of undefined (reading 'focus')
    at Dialog.onAfterAttach (dialog.js:212:1)
    at Dialog.Widget.processMessage (index.es6.js:1445:1)
    at invokeHandler (index.es6.js:444:1)
    at Object.sendMessage (index.es6.js:180:1)
    at Function.attach (index.es6.js:1838:9)
    at dialog.js:130:13
 ```

<!--Describe how you diagnosed the issue. See the guidelines at
 https://jupyterlab.readthedocs.io/en/latest/getting_started/issue.html -->

## Expected behavior

There should be no errors.
<!--Describe what you expected to happen-->

## Context

<!--Complete the following for context, and add any other relevant context-->

- Operating System and version: macOS Big Sure
- Browser and version: Chrome 97.0.4692.7
- JupyterLab version: 3.2.5

