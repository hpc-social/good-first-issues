---
tags: ,type/bug
title: "Issue with local load_profile and %verdi magic"
html_url: "https://github.com/aiidateam/aiida-core/issues/5822"
user: chrisjsewell
repo: aiidateam/aiida-core
---

Locally running the docs build, and thus the tutorial notebook execution, there is now (I don't believe this was originally the case) an issue; that the `Config` does not appear to be "loaded" with the profile, and so verdi tries to load a local default profile. 

```python
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
%verdi node show 1
------------------

---------------------------------------------------------------------------
InvalidOperation                          Traceback (most recent call last)
/var/folders/t2/xbl15_3n4tsb1vr_ccmmtmbr0000gn/T/ipykernel_79897/2387781979.py in <module>
----> 1 get_ipython().run_line_magic('verdi', 'node show 1')

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/IPython/core/interactiveshell.py in run_line_magic(self, magic_name, line, _stack_depth)
   2362                 kwargs['local_ns'] = self.get_local_scope(stack_depth)
   2363             with self.builtin_trap:
-> 2364                 result = fn(*args, **kwargs)
   2365             return result
   2366 

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/decorator.py in fun(*args, **kw)
    230             if not kwsyntax:
    231                 args, kw = fix(args, kw, sig)
--> 232             return caller(func, *(extras + args), **kw)
    233     fun.__name__ = func.__name__
    234     fun.__doc__ = func.__doc__

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/IPython/core/magic.py in <lambda>(f, *a, **k)
    185     # but it's overkill for just that one bit of state.
    186     def magic_deco(arg):
--> 187         call = lambda f, *a, **k: f(*a, **k)
    188 
    189         if callable(arg):

~/Documents/GitHub/aiida_core_develop/aiida/tools/ipython/ipython_magics.py in verdi(self, line, local_ns)
     74         profile = get_profile()
     75         obj = AttributeDict({'config': config, 'profile': profile})
---> 76         return verdi(shlex.split(line), prog_name='%verdi', obj=obj, standalone_mode=False)  # pylint: disable=too-many-function-args,unexpected-keyword-arg
     77 
     78     @magic.needs_local_scope

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in __call__(self, *args, **kwargs)
   1128     def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
   1129         """Alias for :meth:`main`."""
-> 1130         return self.main(*args, **kwargs)
   1131 
   1132 

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in main(self, args, prog_name, complete_var, standalone_mode, windows_expand_args, **extra)
   1052         try:
   1053             try:
-> 1054                 with self.make_context(prog_name, args, **extra) as ctx:
   1055                     rv = self.invoke(ctx)
   1056                     if not standalone_mode:

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in make_context(self, info_name, args, parent, **extra)
    918 
    919         with ctx.scope(cleanup=False):
--> 920             self.parse_args(ctx, args)
    921         return ctx
    922 

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in parse_args(self, ctx, args)
   1611             ctx.exit()
   1612 
-> 1613         rest = super().parse_args(ctx, args)
   1614 
   1615         if self.chain:

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in parse_args(self, ctx, args)
   1376 
   1377         for param in iter_params_for_processing(param_order, self.get_params(ctx)):
-> 1378             value, args = param.handle_parse_result(ctx, opts, args)
   1379 
   1380         if args and not ctx.allow_extra_args and not ctx.resilient_parsing:

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in handle_parse_result(self, ctx, opts, args)
   2332 
   2333             try:
-> 2334                 value = self.process_value(ctx, value)
   2335             except Exception:
   2336                 if not ctx.resilient_parsing:

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in process_value(self, ctx, value)
   2288 
   2289     def process_value(self, ctx: Context, value: t.Any) -> t.Any:
-> 2290         value = self.type_cast_value(ctx, value)
   2291 
   2292         if self.required and self.value_is_missing(value):

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/core.py in type_cast_value(self, ctx, value)
   2276             return tuple(convert(x) for x in check_iter(value))
   2277 
-> 2278         return convert(value)
   2279 
   2280     def value_is_missing(self, value: t.Any) -> bool:

~/Documents/GitHub/aiida_core_develop/.tox/py38-docs-clean/lib/python3.8/site-packages/click/types.py in __call__(self, value, param, ctx)
     80     ) -> t.Any:
     81         if value is not None:
---> 82             return self.convert(value, param, ctx)
     83 
     84     def get_metavar(self, param: "Parameter") -> t.Optional[str]:

~/Documents/GitHub/aiida_core_develop/aiida/cmdline/params/types/profile.py in convert(self, value, param, ctx)
     68 
     69         if self._load_profile:
---> 70             load_profile(profile.name)
     71 
     72         ctx.obj.profile = profile

~/Documents/GitHub/aiida_core_develop/aiida/manage/configuration/__init__.py in load_profile(profile, allow_switch)
    151     """
    152     from aiida.manage import get_manager
--> 153     return get_manager().load_profile(profile, allow_switch)
    154 
    155 

~/Documents/GitHub/aiida_core_develop/aiida/manage/manager.py in load_profile(self, profile, allow_switch)
    124 
    125         if self._profile and self.profile_storage_loaded and not allow_switch:
--> 126             raise InvalidOperation(
    127                 f'cannot switch to profile {profile.name!r} because profile {self._profile.name!r} storage '
    128                 'is already loaded and allow_switch is False'

InvalidOperation: cannot switch to profile 'quicksetup' because profile 'myprofile' storage is already loaded and allow_switch is False
```