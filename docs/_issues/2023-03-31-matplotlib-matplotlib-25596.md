---
tags: Difficulty-Medium,Good-first-issue,Maintenance
title: "[MNT]: Consisteny on Interface"
html_url: "https://github.com/matplotlib/matplotlib/issues/25596"
user: suuuehgi
repo: matplotlib/matplotlib
---

### Summary

```python
D = {ii:ii for ii in range(10)}

fig, ax = plt.subplots()
plt.errorbar(D.keys(), D.values(), D.values())
```
raises the error
```log
TypeError: unsupported operand type(s) for *: 'int' and 'dict_values'
```
while
```python
fig, ax = plt.subplots()
ax.errorbar(D.keys(), D.values(), D.values())
```
works as expected.

(mpl v. 3.5.3)

### Proposed fix

Both work.