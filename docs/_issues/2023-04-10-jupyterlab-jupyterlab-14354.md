---
tags: bug,tagAccessibility
title: "Styled input checkbox focus state is not visible on Ubuntu/Firefox"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/14354"
user: krassowski
repo: jupyterlab/jupyterlab
---

## Description

For checkboxes with `jp-mod-styled` class the focus state is not visible. This might be Operating System specific.

## Reproduce

<!--Describe step-by-step instructions to reproduce the behavior-->

1. Open search box in a notebook
2. Open filters
3. Tab to a checkbox
4. See no focus indication

On Ubuntu/Firefox

![Screenshot from 2023-04-10 15-28-33](https://user-images.githubusercontent.com/5832902/230921695-c89dbd91-8e27-4319-9a1e-3f18f0cd05b3.png)

The one on right is focused.

The styles are defined here:

https://github.com/jupyterlab/jupyterlab/blob/89154f525578e3c79d9f688be1e67605f6d2d443/packages/ui-components/style/styling.css#L45-L48

but it has no effect on styles for me in Firefox on Ubuntu.

Manually adding `outline: 3px solid red;` to `input.jp-mod-styled:focus` shows an indication properly:

![Screenshot from 2023-04-10 15-30-40](https://user-images.githubusercontent.com/5832902/230921881-ceba7417-88d0-4029-a99a-e7f7071fb8c5.png)

Of note, the styles are effective on Ubuntu/Chromium but the indicator is rather faint:

![Screenshot from 2023-04-10 15-36-15](https://user-images.githubusercontent.com/5832902/230923107-7a814346-0064-41d4-8b7b-3298e346c57f.png)

## Expected behavior

Some kind of indicator is visible for checkboxes across browsers

## Context

<!--Complete the following for context, and add any other relevant context-->

- Operating System and version: Ubuntu
- Browser and version: Firefox Nightly 108
- JupyterLab version: 4.0.0b1