---
tags: enhancement,save-files
title: "Add support for saving and restoring procedures"
html_url: "https://github.com/gnudatalanguage/gdl/issues/116"
user: slayoo
repo: gnudatalanguage/gdl
---

As reported by @swrh and discussed with @ebknudsen on SF.net back in 2011 (https://sourceforge.net/p/gnudatalanguage/feature-requests/100/):

The current implementation of SAVE and RESTORE procedures supports saving variables only. IDL allows to save also procedures.

To summarise the discussion (also the one with Marc during the GDL workshop in Paris):
- binary compatibility with IDL is not attainable by design, and is not an aim,
- the key rationale is the potential speed gain due to the option of skipping lengthy compilation of large codebases (effectively, this could be a similar mechanism as the one in Python that produces .pyc files),
- it would be needed to serialise the ProgNode instances.