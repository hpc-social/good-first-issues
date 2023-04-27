---
title: "Add an 'event' command"
html_url: "https://github.com/bluesky/bluesky/issues/941"
user: danielballan
repo: bluesky/bluesky
---

Suggestion by @tacaswell which I am just recording:

Add an `'event'` command so that

```python
Msg('create')
Msg('read', obj1)
Msg('read', obj2)
Msg('save')
```

can be accomplished by

```python
Msg('event', [obj1, obj2])
```

There is really no reason one should need to interleave other commands between these; ~there is no situation we can think of where `'event'` is not sufficient.~ [edit: see next comment] This is a nice simplification.
  