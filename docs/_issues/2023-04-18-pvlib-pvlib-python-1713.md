---
tags: easy
title: "`data` should not be optional in `ModelChain.run_model_from_effective_irradiance`"
html_url: "https://github.com/pvlib/pvlib-python/issues/1713"
user: kandersolar
repo: pvlib/pvlib-python
---

I don't understand why the `data` parameter has a default value of `None` here:

https://github.com/pvlib/pvlib-python/blob/4c24be0475a5fe4c736b0a401a174d295fe75945/pvlib/modelchain.py#L1910

The weather input DataFrame is required for `run_model` and `run_model_from_poa`.  I'm not sure what the point of calling a `run_model_*` method with no inputs might be.  Using the default value of None results in an error:

```python
import pvlib

location = pvlib.location.Location(40, -80)
system = pvlib.pvsystem.PVSystem(module_parameters=dict(pdc0=1, gamma_pdc=-0.004),
                                 inverter_parameters=dict(pdc0=1))

mc = pvlib.modelchain.ModelChain(system, location,
                                 aoi_model='no_loss', spectral_model='no_loss')
mc.run_model_from_effective_irradiance()
```

```
  File ~\software\miniconda3\envs\dev\lib\site-packages\pvlib\modelchain.py:1410 in _verify
    if not set(required) <= set(data.columns):

AttributeError: 'NoneType' object has no attribute 'columns'
```

Seems like the default `None` value should be removed, along with the same for the helper methods (`_run_from_effective_irrad`, etc).