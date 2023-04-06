---
tags: 
title: "error while saving geodataframe as mapinfo .tab file"
html_url: "https://github.com/geopandas/geopandas/issues/967"
user: ghost
repo: geopandas/geopandas
---

Hi,

I'm getting below error while exporting geopandas dataframe as mapinfo .TAB file.

Code:

```
import geopandas as gpd

p=r"D:\data.TAB"
testdata = gpd.read_file(p)
testdata.to_file("output.TAB", driver="MapInfo File")`
```

```
(base) D:\FTTC_Automation\Python\PC_Check\fttc_app>python test.py
Traceback (most recent call last):
  File "fiona\ogrext.pyx", line 1167, in fiona.ogrext.WritingSession.start
  File "fiona\_err.pyx", line 246, in fiona._err.exc_wrap_int
fiona._err.CPLE_AppDefinedError: IMapInfoFile::CreateField() called with unsupported field type 12. Note that Mapinfo files don't support list fiel
d types.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "test.py", line 6, in <module>
    cable.to_file("output.TAB", driver="MapInfo File")
  File "C:\ProgramData\Anaconda3\lib\site-packages\geopandas\geodataframe.py", line 413, in to_file
    to_file(self, filename, driver, schema, **kwargs)
  File "C:\ProgramData\Anaconda3\lib\site-packages\geopandas\io\file.py", line 116, in to_file
    schema=schema, **kwargs) as colxn:
  File "C:\ProgramData\Anaconda3\lib\site-packages\fiona\env.py", line 397, in wrapper
    return f(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\lib\site-packages\fiona\__init__.py", line 267, in open
    **kwargs)
  File "C:\ProgramData\Anaconda3\lib\site-packages\fiona\collection.py", line 162, in __init__
    self.session.start(self, **kwargs)
  File "fiona\ogrext.pyx", line 1173, in fiona.ogrext.WritingSession.start
fiona.errors.SchemaError: IMapInfoFile::CreateField() called with unsupported field type 12. Note that Mapinfo files don't support list field types
```

Any help much appreciated.

Thanks in Advance,
Mani