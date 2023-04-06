---
tags: ,enhancement,stale
title: "Xarray backend to open Argo Netcdf file formats"
html_url: "https://github.com/euroargodev/argopy/issues/176"
user: gmaze
repo: euroargodev/argopy
---

When openning an Argo netcdf file with xarray, most of the variables are not decoded properly and returned as objects.
As shown in the exemple below, 48 out of 64 data variables are not decoded as they should.

So should we implement a new xarray backend to fix this ?

The added value would be that:
- users could use argopy to open files directly, as they want
- argopy machinery would be cleaner if decoding would be done in a single place

## Proposition
Register a new xarray backend for Argo Netcdf files:
```python
import xarray as xr
ds = xr.open_dataset("/Users/gmaze/data/ARGO/ftp_current/dac/aoml/1901393/1901393_prof.nc", engine='argo')
```

To implement this: https://xarray.pydata.org/en/stable/internals/how-to-add-new-backend.html

Since Argopy has already all the necessary snippets implemented in various places, this could easily be packaged I guess.

## The problem
Even with classic decoder options turned on, xarray cannot understand Argo variable type:
```python
import xarray as xr
ds = xr.open_dataset("/Users/gmaze/data/ARGO/ftp_current/dac/aoml/1901393/1901393_prof.nc", 
                     decode_cf=1, use_cftime=1, mask_and_scale=1,)
for v in ds.data_vars:
    print("%30s: %s" % (v, ds[v].data.dtype))
```

```python
                     DATA_TYPE: object
                FORMAT_VERSION: object
              HANDBOOK_VERSION: object
           REFERENCE_DATE_TIME: object
                 DATE_CREATION: object
                   DATE_UPDATE: object
               PLATFORM_NUMBER: object
                  PROJECT_NAME: object
                       PI_NAME: object
            STATION_PARAMETERS: object
                  CYCLE_NUMBER: float64
                     DIRECTION: object
                   DATA_CENTRE: object
                  DC_REFERENCE: object
          DATA_STATE_INDICATOR: object
                     DATA_MODE: object
                 PLATFORM_TYPE: object
               FLOAT_SERIAL_NO: object
              FIRMWARE_VERSION: object
                 WMO_INST_TYPE: object
                          JULD: object
                       JULD_QC: object
                 JULD_LOCATION: object
                      LATITUDE: float64
                     LONGITUDE: float64
                   POSITION_QC: object
            POSITIONING_SYSTEM: object
               PROFILE_PRES_QC: object
               PROFILE_TEMP_QC: object
               PROFILE_PSAL_QC: object
      VERTICAL_SAMPLING_SCHEME: object
         CONFIG_MISSION_NUMBER: float64
                          PRES: float32
                       PRES_QC: object
                 PRES_ADJUSTED: float32
              PRES_ADJUSTED_QC: object
           PRES_ADJUSTED_ERROR: float32
                          TEMP: float32
                       TEMP_QC: object
                 TEMP_ADJUSTED: float32
              TEMP_ADJUSTED_QC: object
           TEMP_ADJUSTED_ERROR: float32
                          PSAL: float32
                       PSAL_QC: object
                 PSAL_ADJUSTED: float32
              PSAL_ADJUSTED_QC: object
           PSAL_ADJUSTED_ERROR: float32
                     PARAMETER: object
     SCIENTIFIC_CALIB_EQUATION: object
  SCIENTIFIC_CALIB_COEFFICIENT: object
      SCIENTIFIC_CALIB_COMMENT: object
         SCIENTIFIC_CALIB_DATE: object
           HISTORY_INSTITUTION: object
                  HISTORY_STEP: object
              HISTORY_SOFTWARE: object
      HISTORY_SOFTWARE_RELEASE: object
             HISTORY_REFERENCE: object
                  HISTORY_DATE: object
                HISTORY_ACTION: object
             HISTORY_PARAMETER: object
            HISTORY_START_PRES: float32
             HISTORY_STOP_PRES: float32
        HISTORY_PREVIOUS_VALUE: float32
                HISTORY_QCTEST: object
```

