---
tags: bug,pkgapputils,tagExtensions
title: "Dialog hangs if IBodyWidget<T>.getValue() throws an error"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/12863"
user: herjiict
repo: jupyterlab/jupyterlab
---

## Description

If `value = body.getValue()` at [dialog.tsx line 431](https://github.com/jupyterlab/jupyterlab/blob/b13556dca76c5b40d22d750d0d5bc97569bcb46f/packages/apputils/src/dialog.tsx#L431) throws an error, then the dialog hangs and cannot be resolved or rejected. Browser refresh is needed.

1. In the `_resolve` method, `this.dispose()` is called after `value = body.getValue()`, so the dialog is not disposed. And `this._promise` is set to `null` before `value = body.getValue()`, so the dialog cannot be rejected.
2. Since [line 178](https://github.com/jupyterlab/jupyterlab/blob/b13556dca76c5b40d22d750d0d5bc97569bcb46f/packages/apputils/src/dialog.tsx#L178) and [line 194](https://github.com/jupyterlab/jupyterlab/blob/b13556dca76c5b40d22d750d0d5bc97569bcb46f/packages/apputils/src/dialog.tsx#L194) return before `_resolve` is called, [line 419](https://github.com/jupyterlab/jupyterlab/blob/b13556dca76c5b40d22d750d0d5bc97569bcb46f/packages/apputils/src/dialog.tsx#L419) is unreachable, and the dialog won't respond to `resolve` or `reject`.

## Reproduce

1. Create an extension and throw an error in `getValue`

```typescript
const plugin: JupyterFrontEndPlugin<void> = {
  id: '@jupyterlab/mytest-extension',
  autoStart: true,
  requires: [ICommandPalette],
  activate: async (app: JupyterFrontEnd, palette: ICommandPalette) => {
    const command = 'mytest-command';
    app.commands.addCommand(command, {
      label: command,
      execute: async () => {
        await showDialog({
          title: 'test',
          body: new (class
            extends Widget
            implements Dialog.IBodyWidget<string> {
            getValue(): string {
              throw new Error('test');
            }
          })()
        });
      }
    });
    palette.addItem({ command, category: 'mytest', args: { isPalette: true } });
  }
};
```

2. Show the dialog. The dialog cannot be resolved or rejected

## Expected behavior

Maybe move `this._promise = null;` and `ArrayExt.removeFirstOf(Private.launchQueue, promise.promise);` between line 432 and line 433, so that users can still at least reject the dialog?

## Context

- Operating System and version: Windows 11 and WSL Ubuntu 20.04
- Browser and version: Edge 103.0.1264.71
- JupyterLab version: 3.4.3