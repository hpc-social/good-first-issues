---
tags: ,help-wanted
title: "fix: avoid scrambling of group members"
html_url: "https://github.com/opencobra/cobrapy/issues/923"
user: BenjaSanchez
repo: opencobra/cobrapy
---

#### Problem description

When going through an I/O cycle with a model that has subsystems stored as groups, the members of each group in the sbml file get scrambled on each cycle, as those members are stored in `set()` structures, which are unordered. This significantly hinders cobrapy to be used for updating a model that has groups and is stored in a Github repository, as hundreds of lines in the sbml file will change order each time the model is saved, even if nothing in the model changes.

Ways in which this could be solved:
1. **Store members in lists instead of sets:** more consistent with the rest of the model objects (mets/rxns/etc.), but could break backwards compatibility with any code out there that directly manipulates members.
2. **Sort the members of each group when saving the model as sbml:** no BC loss, as the member structures would remain as sets. However, it would not respect any eventual predefined order by the user, as the sorting would override it.
3. **Store members in an [`OrderedSet`](https://pypi.org/project/ordered-set/):** a nice middle-ground between the two previous options, but would require an additional dependency.
4. Probably others?

Which way should be preferred? I'm happy to implement the fix, but first recommendations/thoughts from the community would be appreciated :)

#### Code Sample

For a model that has groups:

```python
import cobra
model = cobra.io.read_sbml_model("model.xml")
write_sbml_model(model, "model.xml")
```

#### Actual Output

Example for one of the groups:

![image](https://user-images.githubusercontent.com/9384349/70071541-cc7aeb80-15f5-11ea-85a4-d31d3b7c1984.png)

#### Expected Output

No changes to the model.

#### Dependency Information

<details>

System Information
==================
OS         Windows
OS-release      10
Python       3.7.5
Package Versions
================
cobra                                    0.17.1
depinfo                                   1.5.1
future                                   0.18.2
numpy                                    1.17.4
optlang                                   1.4.4
pandas                                   0.25.3
pip                                      19.3.1
python-libsbml-experimental              5.18.0
ruamel.yaml                              0.16.5
setuptools                  42.0.1.post20191125
six                                      1.13.0
swiglpk                                  4.65.0
wheel                                    0.33.6

</details>
