---
tags: ,ergonomics,models,priority/low,schema,suggestions
title: "Improve response_fields and sort query parameter regexes"
html_url: "https://github.com/Materials-Consortia/optimade-python-tools/issues/808"
user: ml-evs
repo: Materials-Consortia/optimade-python-tools
---

Currently our regexes for `response_fields` and `sort` allow e.g. `response_fields="chemical_formula_anonymous"` through, where the field is treated as the quoted string `'"chemical_formula_anonymous"'`.

This is not ideal and can be fixed in the model regexes directly (which we should then push upstream for v1.0.1 of the spec).

https://github.com/Materials-Consortia/optimade-python-tools/blob/ce8b4ddd1dbdf2a11ab2d8f2457eb2cac6624009/optimade/server/query_params.py#L110-L119
