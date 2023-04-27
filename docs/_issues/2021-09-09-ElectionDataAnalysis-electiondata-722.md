---
tags: technical-debt
title: "Speed up code"
html_url: "https://github.com/ElectionDataAnalysis/electiondata/issues/722"
user: sfsinger19103
repo: ElectionDataAnalysis/electiondata
---

See https://towardsdatascience.com/6-bad-manners-makes-your-python-program-slower-15b6fce62927
- [ ] Replace 'import <module>' with 'from <module> import <item>' where reasonable. Importing a whole module when you're using only part of it can slow things down. 
- [ ] Avoid dot-dot chaining
- [ ] Use for loop,  not while loop, wherever possible