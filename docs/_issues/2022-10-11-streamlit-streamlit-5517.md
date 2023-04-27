---
tags: featurest.progress,priorityP4,statusconfirmed,typebug
title: "Progress Bar Float Error"
html_url: "https://github.com/streamlit/streamlit/issues/5517"
user: spencervoorend
repo: streamlit/streamlit
---

### Summary

streamlit.errors.StreamlitAPIException: Progress Value has invalid value [0.0, 1.0]: 1.000000

### Steps to reproduce

[![Open in Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://issues.streamlitapp.com/?issue=gh-5517)

Code snippet:

```
        count_of_files =  60 
        progress_bar = st.progress(0.0)
        counter = 0
        for file in file_paths:
            print(counter)
            progress_bar.progress(counter + (1/count_of_files))
            counter += float(1/count_of_files)
```



**Expected behavior:**

Should just complete but I suspect it's an issue with floats. 

**Actual behavior:**

Explain the buggy behavior you experience when you go through the steps above.
If applicable, add screenshots to help explain your problem.

### Is this a regression?

That is, did this use to work the way you expected in the past?
 no

### Debug info

- Streamlit version: 1.12.0
- Python version: 3.8.9
- Using Conda? PipEnv? PyEnv? Pex? Poetry
- OS version: MacOS Monterey
- Browser version: Version 105.0.5195.125 (Official Build) (arm64)

### Additional information

If needed, add any other context about the problem here. For example, did this bug come from https://discuss.streamlit.io or another site? Link the original source here!
