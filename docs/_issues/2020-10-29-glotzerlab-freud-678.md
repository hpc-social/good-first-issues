---
tags: environment,order
title: "Check how order parameters treat particles with zero neighbors"
html_url: "https://github.com/glotzerlab/freud/issues/678"
user: bdice
repo: glotzerlab/freud
---

In #672 and #624, we discussed how the Steinhardt order parameter treats particles with zero neighbors. Steinhardt assigns a value of `NaN`. We need to check to see how other methods (Hexatic, Translational, SolidLiquid, LocalDescriptors) handle cases with zero neighbors.

> The follow-up PR would basically be to review freud for other methods where this problem could arise and copy over the test to make sure the same behavior is consistent, as well as updating docs with the note and snippet added here.

_Originally posted by @vyasr in https://github.com/glotzerlab/freud/pull/672#issuecomment-718754948_