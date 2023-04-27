---
tags: refactoring
title: "[REF] Paths Variable in ProfileConverter"
html_url: "https://github.com/tumcms/Open-Infra-Platform/issues/517"
user: jschlenger
repo: tumcms/Open-Infra-Platform
---

**File which is being refactored**
ProfileConverter.h

**Functions**
The profile converter has a protected variable called "paths".
Furthermore, there are various functions that take a "paths" variable as one of the input parameters.
This is not good practice and throws a couple of warnings during compilation.

Please rename the function input variable "paths" to make the code better understandable.
