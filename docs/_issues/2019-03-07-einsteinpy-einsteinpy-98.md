---
tags: performance
title: "jit all the functions which are slow"
html_url: "https://github.com/einsteinpy/einsteinpy/issues/98"
user: shreyasbapat
repo: einsteinpy/einsteinpy
---

🐞 **Problem**

Some methods are tooo slow! For which we brought `einsteinpy.ijit.jit`
🎯 **Goal**
Make einsteinpy fast!
<!--- Why is this change important to you? How would you use it? -->
<!--- How can it benefit other users? -->

💡 **Possible solutions**
Identify the slow methods, and

```
from einsteinpy.ijit import jit

@jit
def ..
```

<!--- Not obligatory, but suggest an idea for implementing addition or change -->

📋  **Steps to solve the problem**

 * Comment below about what you've started working on.
 * Add, commit, push your changes
 * Submit a pull request and add this in comments - `Addresses #<put issue number here>`
 * Ask for a review in comments section of pull request
 * Celebrate your contribution to this project 🎉

P.S : See https://github.com/einsteinpy/einsteinpy/issues/98#issuecomment-583766397
