---
tags: ,Test-Request,hacktoberfest
title: "Test: Symbolic Arithmetic"
html_url: "https://github.com/ianfhunter/GNOLL/issues/171"
user: ianfhunter
repo: ianfhunter/GNOLL
---

**Is your feature request related to a problem? Please describe.**
Legacy Test that needs to be added to our test suit

**Describe the solution you'd like**
a roll of dF! should fail with an error as symbolic dice are not supported for explosions
Add to pytest tests in tests/python

**Describe alternatives you've considered**

**Additional context**

- Subtraction can make no sense for string dice if they do not contain the same items
- You also should not be able to add numbers and strings together
- And you cannot use strings as a condition on numbers
   -  You can do the reverse though.
- String Math does not make sense most of the time

Legacy Tests (may be incorrect/outdated)

| roll | low | high | passes |
| --- | --- | --- | --- |
|"df+df" | -- | ++ | False|
|"10df-2df"| -| ++++++++, |True|
|"2df-20df" |++++++++++++++++++| ------------------|True|
|"d10+df"| -----------| +++++++++++|True|
|"2d4x3df"|----|++++++++++++++++++++++++++++|True|
| "2dF x 2d4"| "--:--"|"++:++:++:++:++:++:++:++"| False|
|"3df!"|---|+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|False|

Error Cases:
"dF*dF"
"dF/dF"
"dF|dF"
"dF%dF"
"dF+dF","--","++",False
"dF-dF"

"dF*d3", "-","+++", False
"dF/d3"
"dF|d3"
"dF%d3"
"dF+d3"
"dF-d3"
