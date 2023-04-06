---
tags: ,component-jupyter,component-python
title: "Save widget settings along with the widget"
html_url: "https://github.com/lab-cosmo/chemiscope/issues/243"
user: rosecers
repo: cosmo-epfl/chemiscope
---

Enable saving of widget settings, so one could call 

```
widget = chemiscope.show(..., settings=dict(...))
widget.save('chemiscope.json.gz')
```
and have the settings save with the widget.