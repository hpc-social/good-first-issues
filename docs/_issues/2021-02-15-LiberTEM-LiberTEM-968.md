---
tags: ,GUI,UX/DX
title: "Floating point input possible for Sig and Nav shape"
html_url: "https://github.com/LiberTEM/LiberTEM/issues/968"
user: uellue
repo: LiberTEM/LiberTEM
---

## How to reproduce

Open an EMPAD file and enter floating point numbers for Nav Shape and Sig Shape. Other file types are not tested but probably are affected, too.

## What happens

The GUI accepts floating point values, which is nonsensical. Text is not accepted. For the sig shape the product has to match, but floating point is still possible. When clicking "Load dataset", the following error is raised:

```
[2021-02-15 22:08:15,132] ERROR [libertem.web.base.log_message:21] message: CREATE_DATASET_ERROR (dataset=f8d8dbe2-5f8c-43be-a5f3-4eb747d94627)
Traceback (most recent call last):
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\libertem\web\dataset.py", line 69, in put
    await self.prime_numba_caches(ds)
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\libertem\web\dataset.py", line 43, in prime_numba_caches
    await executor.run_each_host(functools.partial(prime_numba_cache, ds=ds))
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\libertem\executor\base.py", line 330, in run_each_host
    return await sync_to_async(fn_with_args, self._pool)
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\libertem\executor\base.py", line 231, in sync_to_async
    return await loop.run_in_executor(pool, fn)
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\concurrent\futures\thread.py", line 57, in run
    result = self.fn(*self.args, **self.kwargs)
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\libertem\executor\dask.py", line 358, in run_each_host
    for host, future in future_map.items()
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\libertem\executor\dask.py", line 358, in <dictcomp>
    for host, future in future_map.items()
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\distributed\client.py", line 223, in result
    raise exc.with_traceback(tb)
  File "c:\users\dwebe\.conda\envs\libertem-releasetest\lib\site-packages\libertem\common\numba.py", line 251, in prime_numba_cache
    roi = np.zeros(ds.shape.nav, dtype=np.bool).reshape((-1,))
TypeError: 'float' object cannot be interpreted as an integer
```

After confirming the error message in the GUI, the browse dialogue is closed.

## What should happen

Since the form fields are already validated to only accept numerical input, they should be modified to only accept integers.

Ideally, the dialogue should not close, but allow to correct the input.