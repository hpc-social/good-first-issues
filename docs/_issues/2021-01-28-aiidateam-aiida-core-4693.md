---
tags: ,priority/nice-to-have,topic/verdi,type/feature-request
title: "`verdi calcjob cleanworkdir`: Add option for work chain"
html_url: "https://github.com/aiidateam/aiida-core/issues/4693"
user: mbercx
repo: aiidateam/aiida-core
---

### Is your feature request related to a problem? Please describe

A user on the mailing list wanted to clean the remote directories of all calculation jobs executed within a work chain with `verdi calcjob cleanworkdir`. Currently, this is not possible and I don't think there is a very straightforward way of doing this with the Python API. 

### Describe the solution you'd like

One solution would be to simply add an option, e.g. `--workchains` / `-w`, where the user can provide a list of work chain pks/uuids for which they want the remote directories cleaned:

```
verdi calcjob cleanworkdir -w <WORKCHAIN_ID>
``` 