---
tags: enhancement
title: "File-like object for notice stream"
html_url: "https://github.com/glotzerlab/hoomd-blue/issues/1449"
user: joaander
repo: glotzerlab/hoomd-blue
---

### Description

Provide a Python file-like object that writes to the HOOMD notice message stream.

### Proposed solution

```
device = hoomd.device.CPU()
notice_file = device.make_notice_file(notice_level=1)
notice_file.write("Message\n")

logger = hoomd.logging.Logger()
table_writer = hoomd.write.Table(trigger=hoomd.trigger.Periodic(4000),
                                                         logger=logger,
                                                         output=notice_file)
```

### Additional context

This will allow users to write [`Table` output](https://hoomd-blue.readthedocs.io/en/v3.7.0/module-hoomd-write.html#hoomd.write.Table) to the same output file as [`notice`](https://hoomd-blue.readthedocs.io/en/v3.7.0/module-hoomd-device.html#hoomd.device.Device).

I would use this to include status updates with Table mixed with other status messages printed by `device.notice()` into a separate file for each partition in an aggregate run. `stdout` is mixed from all partitions in aggregate runs.

`notice` accepts one line per call, while `file.write()` accepts arbitrary input. To properly support the file-like protocol, this shim class will need to buffer input, split on lines and issue one `notice()` call per line. 

My main interest for this is adding `notice()` support to `writer.Table`, so a simpler implementation would be to instead make this an option in `Table`:
```
table_writer = hoomd.write.Table(trigger=hoomd.trigger.Periodic(4000),
                                                         logger=logger,
                                                         output='notice')
```
When `output == 'notice'`, `Table` would call `device.notice` instead of `output.write`.