---
tags: ,io
title: "Add variable mapping of read_tmy3"
html_url: "https://github.com/pvlib/pvlib-python/issues/1517"
user: AdamRJensen
repo: pvlib/pvlib-python
---

**Is your feature request related to a problem? Please describe.**
This PR proposes that a `map_variables` parameter be added to the `read_tmy3` function. Additionally, the current `rename_columns` parameter (which removes the units from the column names) should be deprecated. See #714 for a discussion on the topic.

**Describe the solution you'd like**
A `map_variables` parameter should be added (defaulting to None), and if specified as True then it should override the `rename_columns` parameter and map the column names to standard pvlib names. A deperecation warning should be added stating that the `rename_columns` parameter will be retired starting in pvlib 0.11.0 - the deprecation warning should be silenced if `map_variables` is specified as either True or False.
