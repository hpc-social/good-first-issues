---
tags: ,refactor
title: "Clean up module imports"
html_url: "https://github.com/ConnorStoneAstro/AutoProf/issues/23"
user: ConnorStoneAstro
repo: ConnorStoneAstro/AutoProf
---

**Is your refactor request related to a problem? Please describe.**
Currently the imports at the top of each file have been haphazardly placed, added, removed, etc. The order does not conform to any convention and this makes it difficult to find relevant imports, add new ones, or spot redundant imports.

**Describe the solution you'd like**
Imports should be ordered hierarchically. At the top is python imports (like sys and os), then standard packages (numpy, matplotlib, etc), then specific packages (any highly specialized packages such as torch interp1d), then local imports of other autoprof modules.

**Describe alternatives you've considered**
No alternatives should be considered, this is from PEP 8

**Additional context**
This is a standard format from PEP 8: https://peps.python.org/pep-0008/
