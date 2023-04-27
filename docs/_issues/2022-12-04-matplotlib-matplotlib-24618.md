---
tags: Difficulty-Medium,Good-first-issue,New-feature,topic-annotation
title: "[ENH]: \"Road sign\" boxstyle/annotation"
html_url: "https://github.com/matplotlib/matplotlib/issues/24618"
user: oscargus
repo: matplotlib/matplotlib
---

### Problem

Not sure what the proper name is, but it may be useful to have boxstyles as below (red part, black is the object if encloses):
![image](https://user-images.githubusercontent.com/8114497/205505978-d893b425-8d1f-44b9-85aa-910928ad19fc.png)





### Proposed solution

Add boxstyles/annotiation styles as above.

As there already are arrow styles, these should be called something else.

Also, one may consider what `pad` should mean here. Probably the left alternative where the "arrow side" is not padded (as opposed to the right alternative). Should one be possible to provide the angle or should it always be 45 degrees?

Is there a use for a double-arrowed version?