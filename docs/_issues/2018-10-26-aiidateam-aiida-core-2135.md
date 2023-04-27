---
tags: priority/nice-to-have,topic/orm
title: "orm.Computer define class constants for all properties"
html_url: "https://github.com/aiidateam/aiida-core/issues/2135"
user: muhrin
repo: aiidateam/aiida-core
---

Currently a couple of computer properties have class constants that store the corresponding name e.g. `PROPERTY_WORKDIR = 'workdir'`.  This should be extended for all properties e.g. `mpirun_command`.