---
tags: 
title: "Remote logging does not format %s placeholders"
html_url: "https://github.com/multiscale/muscle3/issues/149"
user: maarten-ic
repo: multiscale/muscle3
---

**Reproduction:**

1. In `docs/source/examples/python/reaction.py` add a logging statement in the reuse loop with a `%s` placeholder, for example `logging.warning("Reusing %s instance", "reaction")`
2. Run the examples (`make test_examples`)
3. Check output of `run_reaction_diffusion_python_<date>_<time>`:
   - `instances/micro/stderr.txt` displays `Reusing reaction instance`, as expected
   - `muscle3_manager.log` displays `Reusing %s instance`

**Expected behaviour:**

The muscle manager logs should also show the formatted message.

**To fix:**

Format the message in `MuscleManagerHandler` before creating the LogMessage. See for example the python [StreamHandler.emit implementation here](https://github.com/python/cpython/blob/b99ac1dbc081e4f2d2e68906e9c7c535e628611a/Lib/logging/__init__.py#L1098).