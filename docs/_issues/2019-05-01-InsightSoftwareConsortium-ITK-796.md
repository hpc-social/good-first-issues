---
tags: ,Good-first-issue,typeDocumentation
title: "Standardize documentation in `Utilities` scripts"
html_url: "https://github.com/InsightSoftwareConsortium/ITK/issues/796"
user: jhlegarreta
repo: InsightSoftwareConsortium/ITK
---

### Description

The [`Utilities`](https://github.com/InsightSoftwareConsortium/ITK/tree/master/Utilities) and [`Utilities/Maintenance`](https://github.com/InsightSoftwareConsortium/ITK/tree/master/Utilities/Maintenance) folders contain a number of scripts that are important both to ease a number of tasks related to the toolkit and to keep the toolkit healthy.

However, many of the lack a proper documentation. There is some truth in that only a limited number of people (mainly maintainers) use them effectively, but even then, it may be worthwhile properly documenting them.

If they **followed some standard, the documentation could be rendered on a web page, much like the Doxygen class documentation, and thus the purpose and use of the scripts would be accessible**. That would allow for a more effective information hand-off to new maintainers, or other community members could be aware of such scripts to apply them in some parts of the toolkit (e.g. remotes, third parties, etc.).

### Expected information

Proper/canonical script documentation (both header-like comment and usage help message, following some documentation standard if possible, e.g.:

https://stackoverflow.com/questions/14008125/shell-script-common-template
https://unix.stackexchange.com/questions/6891/how-can-i-add-man-page-entries-for-my-own-power-tools

having some mandatory sections/fields:

- `NAME`
- `SYNOPSIS`
- `DESCRIPTION`
- `OPTIONS`
- `IMPLEMENTATION`
- `EXAMPLES`
- `SEE ALSO`

and formatting.

With a result that could look like:
https://linux.die.net/man/7/groff_man

If this is something that could be automated, it would be nice. Otherwise, it will need to be done manually.

Also, if this is made effective, the ITK Software Guide will need to contain a section dedicated to documenting how the bash scripts and their usage needs to be ideally written (`#!/bin/bash` lines, copyright notice, arguments, if named or required, etc.) and documented (script header, script usage, etc.).

### Actual information

Maintenance scripts lacking proper documentation and/or no standards followed to document scripts.

### Versions

`master`. 

If the commit number is required, run `$ git rev-parse --short HEAD`. -->

### Additional Information

None.