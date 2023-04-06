---
tags: ,Docs,IO-CSV,Performance,Timeseries
title: "DOC: Reccomended use of read_csv's date_parser parameter is very slow"
html_url: "https://github.com/pandas-dev/pandas/issues/35296"
user: sm-Fifteen
repo: pandas-dev/pandas
---



#### Location of the documentation

The [Date parsing functions](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#date-parsing-functions) section of the CSV file parsing section, specifically the reccomended use of `date_parser` in cases where the user knows what format the date will be in in advance and/or that format is non-standard ans not supported by Pandas.

> If you know the format, use `pd.to_datetime()`: `date_parser=lambda x: pd.to_datetime(x, format=...)`.

#### Demonstration of the problem

<details>
I'm trying to parse a CSV file that contains signal power data keyed by timestamp-frequency pairs in a vertical format (376 frequencies by 14300 samples, so about 5.3 million rows, with only one timestamp per row) with the intent of pivoting it into a columnar format. The time format is rather unpleasant to deal with and is stored as 2 separate columns, but pandas' CSV parser has all the tools I need to reconstruct the timestamps correctly, so I'm not worried there.

Based on what the documentation, I tried something like this:

```py
import pandas as pd

def read_csv_slow(in_path: str):
    df = pd.read_csv(
        in_path,
        nrows=376 * 500,
        usecols=['Date','Time', 'Frequency', 'Power'], index_col=['Date_Time', 'Frequency']
        dtype={'Frequency': 'int32', 'Power': 'float32'},

       parse_dates=[['Date','Time']],

        # Extremely slow
        date_parser=lambda x: pd.to_datetime(x, format='%m/%d/%Y %H:%M:%S:%f'), # 06/17/2020 + 11:47:22:746
    )
```

For testing, I limited the amount of rows parsed to 500 time samples (188000 rows/timestamps), about 3.5% of the total file, which takes a surprising 43 seconds to process, mostly due to datetime parsing according to `cProfile`:

```
> python -m cProfile -s tottime .\read_csv_slow.py
         61508066 function calls (61501857 primitive calls) in 43.756 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   188000    4.507    0.000    5.728    0.000 {pandas._libs.tslibs.strptime.array_strptime}
 15247920    3.286    0.000    5.884    0.000 {built-in method builtins.isinstance}
   188000    2.358    0.000    2.358    0.000 {pandas._libs.tslibs.parsing._format_is_iso}
  5264920    1.851    0.000    2.432    0.000 generic.py:10(_check)
  1316199    1.828    0.000    3.879    0.000 common.py:1708(_is_dtype_type)
   188001    1.650    0.000   34.982    0.000 datetimes.py:246(_convert_listlike_datetimes)
   376150    1.400    0.000    1.400    0.000 {built-in method numpy.array}
   188006    1.348    0.000    8.870    0.000 datetimes.py:1678(sequence_to_dt64ns)
   188001    1.292    0.000   42.474    0.000 datetimes.py:530(to_datetime)
```

Using `date_parser` like this simply does not scale and blocks the entire CSV decoding process.

----

Meanwhile, here's an alternative version that bypasses `date_parser` and converts the datetime column in a single batch after parsing finishes:

```py
import pandas as pd

def read_mxflex_csv_fast(in_path: str):
    df = pd.read_csv(
        in_path,
        nrows=376 * 10000,
        usecols=['Date','Time', 'Frequency', 'Power'], index_col=['Date_Time', 'Frequency']
        dtype={'Frequency': 'int32', 'Power': 'float32'},

       parse_dates=[['Date','Time']],
    )

    date_data = df.index.get_level_values(0)
    date_idx = pd.to_datetime(date_data, exact=True, cache=True, format='%m/%d/%Y %H:%M:%S:%f') # 06/17/2020 + 11:47:22:746
    freq_idx = df.index.get_level_values(1)
    df.index = pd.MultiIndex.from_arrays([date_idx, freq_idx])
```

This one completes in 6 seconds despite running on *20 times as much data* (10000 samples instead of 500, notice the change in `nrows`) than the first example.

```
> python -m cProfile -s tottime .\read_csv_fast.py
         236167 function calls (229787 primitive calls) in 5.957 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.353    2.353    2.412    2.412 {method 'read' of 'pandas._libs.parsers.TextReader' objects}
       28    0.477    0.017    0.477    0.017 {pandas._libs.lib.infer_dtype}
        2    0.442    0.221    0.442    0.221 {method 'unique' of 'pandas._libs.hashtable.StringHashTable' objects}
        1    0.344    0.344    0.344    0.344 {pandas._libs.tslibs.parsing._concat_date_cols}
        2    0.342    0.171    0.342    0.171 {method 'get_indexer' of 'pandas._libs.index.IndexEngine' objects}
        1    0.235    0.235    0.235    0.235 {method 'factorize' of 'pandas._libs.hashtable.StringHashTable' objects}
       60    0.179    0.003    0.182    0.003 {built-in method _imp.create_dynamic}
     1667    0.177    0.000    0.177    0.000 {built-in method nt.stat}
        3    0.136    0.045    0.136    0.045 {method 'factorize' of 'pandas._libs.hashtable.Int64HashTable' objects}
```
</details>

#### Documentation problem

Usage of the `date_parser` parameter tends to be a *huge* performance cliff given how it appears to run in an row-wise fashion (if the profiler's `ncalls` metric is to be believed), something the surrounding documentation heavily stresses as well:

> If you have `parse_dates` enabled for some or all of your columns, and your datetime strings are all formatted the same way, you may get a large speed up by setting `infer_datetime_format=True`. If set, pandas will attempt to guess the format of your datetime strings, and then use a faster means of parsing the strings. 5-10x parsing speeds have been observed.

The speedup described there isn't from Pandas having some sort of inferred date fast-path, but simply because the `date_parser` callback is being called in an extremely inefficient way for most workloads. There *is* a note above that section that could be considered as hinting at this:

> If a column or index contains an unparsable date, the entire column or index will be returned unaltered as an object data type. For non-standard datetime parsing, use `to_datetime()` after `pd.read_csv`.

All of those conflicting advices makes the current documentation fairly misleading on that topic, and people who don't profile their code might be led to believe that this is just a problem with pandas being too slow to handle their CSVs or something along those lines.

#### Suggested fix for documentation

One subsection of the Date Handling section (either appended to "Date parsing functions" or under a new subtitle) should give concrete examples on how to deal with files that contain non-standard or strange timestamp formats.

> If your CSV file contains columns with timestamps in an unconventional format, it is usually significantly faster to
> completely parse the file while leaving your dates as text (rather than specifying a `date_parser` callback when opening the file) and later converting the entire column as a single manipulation.
> 
> ```
> print(open('buzz.csv').read())
> Date,Time,Value
> 11261999,13h57m58s.345,0.0100
> 11261999,13h57m59s.999,-0.5900
> ```
> 
> ```
> ts_format = "%m%d%Y %Hh%Mm%Ss.%f" # 11261999 13h57m59s.999
> 
> df = pd.read_csv('buzz.csv' parse_dates=[['Date','Time']], index_col=['Date_Time'],  infer_datetime_format=False)
> df.index = pd.to_datetime(df.index, exact=True, cache=True, format=ts_format)
> ```

This gives clear instructions for users dealing with a use case that's probably not all that uncommon, mentions the alternative and a reason why this is preferable and gives a code example. The code example itself also shows the interaction between `parse_dates` when combining columns and manually-specified date formats (the doc does not otherwise mention that this results in a column of space-separated values). I'm not certain how to change the above code example to make it work correctly for data columns, index columns and multi-indexes alike, if such a thing is possible.