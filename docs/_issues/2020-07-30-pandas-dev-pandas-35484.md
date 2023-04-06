---
tags: ,IO-SQL,Needs-Tests
title: "BUG: read_sql no longer works simply with SqlAlchemy selectables and a quick fix"
html_url: "https://github.com/pandas-dev/pandas/issues/35484"
user: machow
repo: pandas-dev/pandas
---

- [x] I have checked that this issue has not already been reported.

- [x] I have confirmed this bug exists on the latest version of pandas.

- [x] (optional) I have confirmed this bug exists on the master branch of pandas.

---

#### Code Sample, a copy-pastable example

Hey--I noticed while running [siuba's](https://github.com/machow/siuba) SQL unit tests that queries using the modulo operator are failing.

The issue is due to a recent change for issue #34211 in pandas setting the [no_parameters](https://github.com/pandas-dev/pandas/blame/5507452c4a675ad5453bc5f02cd68b65fe3977df/pandas/io/sql.py#L1161) argument before executing via a sqlalchemy engine. This was done to allow queries like `SELECT 1 % 2`, but causes SqlAlchemy expressions handling `%` to not always work with `read_sql`.

**Solution**. Rather than executing in a special way (`no_parameters`), I think you want to wrap a string query in SqlAlchemy.sql.text ([see here](https://docs.sqlalchemy.org/en/13/core/tutorial.html#using-textual-sql)). This will allow both queries with `%` and the full range of SqlAlchemy expressions. WDYT?

```python
from sqlalchemy import sql, create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:@localhost:5433/postgres', echo=False)
#engine = create_engine('postgresql://USERNAME:PASSWORD@localhost:PORT/DBNAME', echo=False)

# doesn't work, original issue in pandas: 'dict' object does not support indexing
engine.execute("SELECT 1 % 2")

# works, ideal solution
engine.execute(sql.text("SELECT 1 % 2" ))

# queries below broken by no_parameters change ----
pd.read_sql(sql.text("SELECT 1 % 2"), engine)

pd.read_sql(sql.select([sql.literal(1) % sql.literal(2)]), engine)
```

Here's a gist of the error for the last two queries...

```
ProgrammingError: (psycopg2.errors.UndefinedFunction) operator does not exist: integer %% integer
LINE 1: SELECT 1 %% 2
                 ^
HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.

[SQL: SELECT 1 %% 2]
(Background on this error at: http://sqlalche.me/e/13/f405)
```

Full traceback in the details

<details>
```
---------------------------------------------------------------------------
UndefinedFunction                         Traceback (most recent call last)
~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
   1267                     self.dialect.do_execute_no_params(
-> 1268                         cursor, statement, context
   1269                     )

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/default.py in do_execute_no_params(self, cursor, statement, context)
    595     def do_execute_no_params(self, cursor, statement, context=None):
--> 596         cursor.execute(statement)
    597 

UndefinedFunction: operator does not exist: integer %% integer
LINE 1: SELECT 1 %% 2
                 ^
HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.


The above exception was the direct cause of the following exception:

ProgrammingError                          Traceback (most recent call last)
<ipython-input-6-5831ea4e198c> in <module>
----> 1 pd.read_sql(sql.text("SELECT 1 % 2"), engine)

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/pandas/io/sql.py in read_sql(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize)
    513             coerce_float=coerce_float,
    514             parse_dates=parse_dates,
--> 515             chunksize=chunksize,
    516         )
    517 

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/pandas/io/sql.py in read_query(self, sql, index_col, coerce_float, parse_dates, params, chunksize)
   1293         args = _convert_params(sql, params)
   1294 
-> 1295         result = self.execute(*args)
   1296         columns = result.keys()
   1297 

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/pandas/io/sql.py in execute(self, *args, **kwargs)
   1160         """Simple passthrough to SQLAlchemy connectable"""
   1161         return self.connectable.execution_options(no_parameters=True).execute(
-> 1162             *args, **kwargs
   1163         )
   1164 

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/base.py in execute(self, statement, *multiparams, **params)
   2236 
   2237         connection = self._contextual_connect(close_with_result=True)
-> 2238         return connection.execute(statement, *multiparams, **params)
   2239 
   2240     def scalar(self, statement, *multiparams, **params):

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/base.py in execute(self, object_, *multiparams, **params)
   1012             )
   1013         else:
-> 1014             return meth(self, multiparams, params)
   1015 
   1016     def _execute_function(self, func, multiparams, params):

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/sql/elements.py in _execute_on_connection(self, connection, multiparams, params)
    296     def _execute_on_connection(self, connection, multiparams, params):
    297         if self.supports_execution:
--> 298             return connection._execute_clauseelement(self, multiparams, params)
    299         else:
    300             raise exc.ObjectNotExecutableError(self)

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_clauseelement(self, elem, multiparams, params)
   1131             distilled_params,
   1132             compiled_sql,
-> 1133             distilled_params,
   1134         )
   1135         if self._has_events or self.engine._has_events:

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
   1316         except BaseException as e:
   1317             self._handle_dbapi_exception(
-> 1318                 e, statement, parameters, cursor, context
   1319             )
   1320 

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _handle_dbapi_exception(self, e, statement, parameters, cursor, context)
   1510             elif should_wrap:
   1511                 util.raise_(
-> 1512                     sqlalchemy_exception, with_traceback=exc_info[2], from_=e
   1513                 )
   1514             else:

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/util/compat.py in raise_(***failed resolving arguments***)
    176 
    177         try:
--> 178             raise exception
    179         finally:
    180             # credit to

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
   1266                 if not evt_handled:
   1267                     self.dialect.do_execute_no_params(
-> 1268                         cursor, statement, context
   1269                     )
   1270             else:

~/Dropbox/Repo/siuba/env/lib/python3.6/site-packages/sqlalchemy/engine/default.py in do_execute_no_params(self, cursor, statement, context)
    594 
    595     def do_execute_no_params(self, cursor, statement, context=None):
--> 596         cursor.execute(statement)
    597 
    598     def is_disconnect(self, e, connection, cursor):

ProgrammingError: (psycopg2.errors.UndefinedFunction) operator does not exist: integer %% integer
LINE 1: SELECT 1 %% 2
                 ^
HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.

[SQL: SELECT 1 %% 2]
(Background on this error at: http://sqlalche.me/e/13/f405)
```

</details>

