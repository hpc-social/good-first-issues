---
tags: ,documentation
title: "Documentation overhaul"
html_url: "https://github.com/einsteinpy/einsteinpy/issues/630"
user: JeS24
repo: einsteinpy/einsteinpy
---

 ### 🐞**Problem**
(Moved from #614)

We need help with the following with respect to the API documentation ("API reference") of the various EinsteinPy submodules:
1. Fixing grammatical errors and making the wording simpler at certain places.
2. Expanding the current documentation, something like what [`sunpy`](https://docs.sunpy.org/en/stable/code_ref/index.html) or [`astropy`](https://docs.astropy.org/en/stable/constants/index.html) API references read like.
3. Adding new example Jupyter notebooks that serve as tutorials or improving old ones. (See also #626). 

Some good starting points are perhaps the docs for the following submodules:
* [ ] [`coordinates`](https://docs.einsteinpy.org/en/latest/api/coordinates/coordinates_index.html)
* [ ] [`integrators`](https://docs.einsteinpy.org/en/latest/api/integrators/integrators_index.html)
* [ ] [`metric`](https://docs.einsteinpy.org/en/latest/api/metric/metric_index.html)
* [ ] [`symbolic`](https://docs.einsteinpy.org/en/latest/api/symbolic/symbolic_index.html)
* [ ] [`geodesic`](https://docs.einsteinpy.org/en/latest/api/geodesic/geodesic.html)

#### ‼️ As the issue title suggests, this is a major reshuffle, which will likely require multiple people working on several pull requests. ***So, please feel free to work on any part of the docs and open Pull Requests, no matter the size of the contribution***.

### ❕ **Relevant information**

* The source for the EinsteinPy docs can be found here: https://github.com/einsteinpy/einsteinpy/tree/main/docs/source/api, while the compiled docs are available at https://docs.einsteinpy.org/en/latest/api/index.html.
*  If you want to know what the code does, a good place to start would be the [`source/examples/`](https://github.com/einsteinpy/einsteinpy/tree/main/docs/source/examples) folder, since it contains tutorials in the form of Jupyter notebooks. You can run the code there and understand what it is doing. You can then use that knowledge to improve the API docs (at least for the parts of the API present in the tutorials).
* We use reStructuredText (reST) for writing the docs in the `numpydoc` style. You can find a quick primer on reST here: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html, while an example of the `numpydoc` style is available here: https://numpydoc.readthedocs.io/en/latest/example.html.

 ### 📋**Steps to solve the problem**

Please consult the [developer docs](https://docs.einsteinpy.org/en/latest/dev_guide.html) to setup your dev environment and get started. Also, feel free to communicate, if you hit a snag. You can do so in our [Gitter](https://gitter.im/EinsteinPy-Project/EinsteinPy) or [Matrix/Element](https://matrix.to/#/#einsteinpy:matrix.org) chat rooms (recommended), or you can also reply here.

 * Comment below about what you've started working on.
 * Add, commit, push your changes
 * Submit a pull request.
 * Add this in the comments:
 	- `Addresses #<put issue number here>` if you are partially fixing the issue.
 	- `Fixes #<put issue number here>` if you are completely fixing the issue.
 * Ask for a review in comments section of pull request
 * Celebrate your contribution to this project 🎉