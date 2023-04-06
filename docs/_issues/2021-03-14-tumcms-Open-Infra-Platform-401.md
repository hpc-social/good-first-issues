---
tags: ,IFC,bug,early-binding-generator
title: "[BUG] Spaces get removed from literal text when reading IFC"
html_url: "https://github.com/tumcms/Open-Infra-Platform/issues/401"
user: pjanck
repo: tumcms/Open-Infra-Platform
---

**Describe the bug**
When reading IFC content, all literal strings get their spaces removed.

**Expected behavior**
Spaces within literal strings remain intact.

**Additional context**
I assume the responsible code is:

https://github.com/tumcms/Open-Infra-Platform/blob/0b29b101f4948b43fd914a3243249ea012c9ec42/ExpressBindingGenerator/src/Generator/GeneratorOIP.cpp#L2175
