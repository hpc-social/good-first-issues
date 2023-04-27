---
tags: enhancement
title: "Add \"%>%\" pipe and \"<-\" assignment when using IRkernel in JupyterLab"
html_url: "https://github.com/jupyterlab/jupyterlab/issues/11194"
user: k-motwani
repo: jupyterlab/jupyterlab
---

Would it be possible to incorporate these into JupyterLab shortcuts out of the box? New to GH but longtime reader - please let me know how I can help. Thank you!


This was previously tracked in https://github.com/jupyterlab/jupyterlab/issues/4519, but appears that it was never documented (outside of changelog). I think that we should document how to make adjustments like that possible. In particular, thanks to https://github.com/jupyterlab/jupyterlab/pull/7908 you can configure your keyboard shortcuts for R with the following:

```json
{
    "shortcuts": [
        {
            "command": "apputils:run-first-enabled",
            "selector": "body",
            "keys": ["Alt -"],
            "args": {
                "commands": [
                    "console:replace-selection",
                    "fileeditor:replace-selection",
                    "notebook:replace-selection",
                ],
                "args": {"text": "<- "}
            }
        },
        {
            "command": "apputils:run-first-enabled",
            "selector": "body",
            "keys": ["Accel Shift M"],
            "args": {
                "commands": [
                    "console:replace-selection",
                    "fileeditor:replace-selection",
                    "notebook:replace-selection",
                ],
                "args": {"text": "%>% "}
            }
        }
    ]
}
```

`Accel` means <kbd>Ctrl</kbd> on Linux and Windows, or <kbd>Command</kbd> on Mac.

Just go to the `Advanced Settings Editor` -> `Keyboard Shortcuts`, paste and save:

![rstudio](https://user-images.githubusercontent.com/5832902/115147572-88a24e00-a053-11eb-9a2e-2b44cece41d4.gif)

PS. You will need a modern JupyterLab version, at least 2.1+ (I usually recommend the latest, currently 3.0).

_Originally posted by @krassowski in https://github.com/jupyterlab/jupyterlab/issues/10114#issuecomment-821993321_