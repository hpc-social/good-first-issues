---
tags: 
title: "Improvements to coordinate_transform.py"
html_url: "https://github.com/mosdef-hub/mbuild/issues/884"
user: jennyfothergill
repo: mosdef-hub/mbuild
---

TODO comments from `mbuild/coordinate_transform.py`
```
329:        # TODO: vstack is slow, replace with list concatenation
330-        if not pair[0].children:
331-            self_points = np.vstack([self_points, pair[0].pos])
332-            other_points = np.vstack([other_points, pair[1].pos])

383-            if not from_positions.anchor or not to_positions.anchor:
384:                # TODO: I think warnings is undefined here
385-                warn("Attempting to form bond from port that has no anchor")

403:    TODO: -Increase robustness for cases where the anchors are a different
404-           distance from their respective ports.
405-          -Provide options in `force_overlap` to override this behavior.
```
related to #872