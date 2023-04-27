---
tags: argo-traj,enhancement,stale
title: "New method to fetch data along a given trajectory"
html_url: "https://github.com/euroargodev/argopy/issues/169"
user: gmaze
repo: euroargodev/argopy
---

## Motivation
For some Argo data analysis it could be useful to be able to fetch data `around` some specific locations, eg: 

- compare some float data with neighbor floats (any QC would do this, but also sensor dev. see eg from @matdever #168 )

- co-localise Argo float profiles with some Huricane path  ([eg here]( http://arashi.geosci.msstate.edu/tropical/2021/Argo2021.html) from [Kim Wood](https://twitter.com/DrKimWood ) )

it could be useful to have an access point that directly fetch this.

## API for new access point
It could look like this:
```python
from argopy import DataFetcher as ArgoDataFetcher

# Default temporal distance is 'days' and radial distance unit is 'degree':
neighbor_fetcher = ArgoDataFetcher(ds='phy').around(wmo=[6903754], dt=365, dr=1)  # All float trajectory
neighbor_fetcher = ArgoDataFetcher(ds='phy').around(wmo=[6903754], cyc=[12], dt=365, dr=1)  # Single profile
neighbor_fetcher = ArgoDataFetcher(ds='phy').around(wmo=[6903754], cyc=[12,13,14], dt=365, dr=1)  # Selected profiles

# Possibly distinguish zonal and meridional distances:
neighbor_fetcher = ArgoDataFetcher(ds='ref').around(wmo=[6903754], dt=30, dx=2, dy=1) 

# Use option to change units:
neighbor_fetcher = ArgoDataFetcher(ds='ref').around(wmo=[6903754], dt=30, dx=100, dy=50, unit='km')

# Get data/index the classic way:
neighbor_ds = neighbor_fetcher.load().data

# argopy would add new variables to the fetched data, like distances to the requested reference profiles:
neighbor_ds['distance_time']
neighbor_ds['distance_radial']
neighbor_ds['distance_zonal']
neighbor_ds['distance_meridional']
```

This new access point, could in fact take a path or trajectory as input:
```python
from argopy import DataFetcher as ArgoDataFetcher

# [2021 Hurricane Larry](https://www.nhc.noaa.gov/data/tcr/index.php?season=2021&basin=atl)
traj = [[-26.00,12.00,'2021-09-01 12:00:00'],[-33.00,13.00,'2021-09-02 12:00:00'],[-40.00,14.00,'2021-09-03 12:00:00'],[-45.00,16.00,'2021-09-04 12:00:00'],[-49.00,19.00,'2021-09-05 12:00:00'],[-52.00,21.00,'2021-09-06 12:00:00'],[-55.00,24.00,'2021-09-07 12:00:00'],[-57.00,27.00,'2021-09-08 12:00:00'],[-61.00,31.00,'2021-09-09 12:00:00'],[-61.00,38.00,'2021-09-10 12:00:00'],[-49.00,52.00,'2021-09-11 12:00:00']]

neighbor_fetcher = ArgoDataFetcher(ds='phy').around(path=traj, dt=5, dr=50, unit='km')
```

## Further
Note this API could easily be plugged into the ``argo`` access point:
```python
from argopy import DataFetcher as ArgoDataFetcher

float_fetcher = ArgoDataFetcher(ds='phy').float(6903754)
float_ds = fetcher.load().data

neighbor_ds = float_ds.argo.around(dt=365, dr=1)
neighbor_ds = float_ds.argo.around(dt=365, dx=2, dy=1) 
neighbor_ds = float_ds.argo.around(dt=365, dx=100, dy=50, unit='km')
neighbor_ds = float_ds.argo.around(dt=365, dr=1, ds='ref')  # Fetch data from the Argo CTD reference
```
