---
tags: enhancement
title: "add automatic authorization to order/download"
html_url: "https://github.com/icesat2py/icepyx/issues/411"
user: JessicaS11
repo: icesat2py/icepyx
---

with the addition of earthaccess in #410, authentication is greatly simplified on the icepyx side and no longer requires any user-input arguments. We could now eliminate the requirement for a `Query.earthdata_login()` step. Tasks:
- [ ] add this capability by doing an authentication check at the start of `Query.order_data()`.
- [ ] update docs accordingly
- [ ] update examples to note this improvement