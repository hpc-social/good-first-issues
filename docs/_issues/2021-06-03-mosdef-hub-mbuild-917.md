---
title: "Document required vs. optional dependencies"
html_url: "https://github.com/mosdef-hub/mbuild/issues/917"
user: mattwthompson
repo: mosdef-hub/mbuild
---

**Describe the behavior you would like added to mBuild**
It would be useful for both users and downstream developers to have quick access to which dependencies are required and optional. One can infer this from what's pulled in and not pulled in with a vanilla install, but packaging complexity can obfuscate the difference between the two.

**Describe the solution you'd like**
The ["Supported Python Versions"](https://mbuild.mosdef.org/en/stable/installation.html#supported-python-versions) section of the installation page does precisely what I'd be after here. (This page might be out of date now, actually, but it's the type of  information presented in the right place, I think.)

**Describe alternatives you've considered**
One can guess what is optional, required, test-/dev-facing, etc. by inspecting various YAML files here and in the feedstock. Ideally this information should be in the docs in plaintext as well.

**Additional context**
It can be easy for these to get out of sync in their various locations, but IMO it's worth it overall.