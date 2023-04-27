---
tags: refactoring
title: "[REF] noexcept(false) in IfcGeometryConverter"
html_url: "https://github.com/tumcms/Open-Infra-Platform/issues/518"
user: jschlenger
repo: tumcms/Open-Infra-Platform
---

**File which is being refactored**
All files that belong to the IfcGeometryConverter.

**Functions**
With the update to VS2019 the throw keyword (throw(...)) right after the specification of the input parameters of a function should be replaced with "noexcept(false)".

Some files of the IfcGeometryConverter already got changed accordingly, but there are still various files where this is left to do.
