---
tags: docs
title: "Improve description of modifier inputs in docs"
html_url: "https://github.com/scikit-hep/pyhf/issues/1410"
user: matthewfeickert
repo: scikit-hep/pyhf
---

# Description

At the [PyHEP April 2021 topical meeting `pyhf` tutorial](https://indico.cern.ch/event/985425/), @BlaiseDelaney had the following question on pertaining to the [Normalisation Uncertainty (normsys) docs](https://pyhf.readthedocs.io/en/v0.6.1/likelihood.html#normalisation-uncertainty-normsys):

> I'm a bit confused about what I need to supply to the modifier. Is it the actual numerical values of the 1 sigma bounds from the Gaussian constraint yields?

We should probably clear in very explicit text what the values given to the modifier in the model spec represent (absolute count vs. relative scale factor). 

At [the moment in the docs](https://github.com/scikit-hep/pyhf/blob/0588b2126e1bf19e6b7d9e00eb75d55dff535142/docs/likelihood.rst) we have:

```rst
Normalisation Uncertainty (normsys)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The normalisation uncertainty modifies the sample rate by a overall
factor :math:`\kappa(\alpha)` constructed as the interpolation between
downward ("lo") and upward ("hi") as well as the nominal setting, i.e.
:math:`\kappa(-1) = \kappa_{\alpha=-1}`, :math:`\kappa(0) = 1` and
:math:`\kappa(+1) = \kappa_{\alpha=+1}`. In the modifier definition we record
:math:`\kappa_{\alpha=+1}` and :math:`\kappa_{\alpha=-1}` as floats. An
example is shown below:

.. code:: json

   { "name": "mod_name", "type": "normsys", "data": {"hi": 1.1, "lo": 0.9} }

An example of a normalisation uncertainty modifier with scale factors recorded for the up/down variations of an :math:`n`-bin channel.
```

but I can see how this could benefit with some more explicit statements about the `kappa`s as well as maybe linking back to the [Modifiers and Constraints table in the HistFactory spec section of the Introduction](https://pyhf.readthedocs.io/en/v0.6.1/intro.html#id24).

The [modifier API docs could use improvement as well](https://pyhf.readthedocs.io/en/v0.6.1/_generated/pyhf.modifiers.normsys.html).