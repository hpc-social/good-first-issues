---
tags: featurest.secrets,priorityP2,statusconfirmed,typebug
title: "\"Missing secrets.toml\" error message is printed incorrectly in Windows"
html_url: "https://github.com/streamlit/streamlit/issues/6147"
user: vdonato
repo: streamlit/streamlit
---

### Checklist

- [X] I have searched the [existing issues](https://github.com/streamlit/streamlit/issues) for similar issues.
- [X] I added a very descriptive title to this issue.
- [X] I have provided sufficient information below to help reproduce this issue.

### Summary

In windows, the message printed when a user tries to access an element in `st.secrets` without having defined a `secrets.toml` file is incorrect.

This is because the path separator character in Windows is `\`, which is interpreted by `st.error` as a markdown escape.

### Reproducible Code Example

```Python
# On a Windows machine

import streamlit as st

# *Without* a secrets.toml file in the CWD
st.secrets["nonexistent"]
```


### Steps To Reproduce

1. Run the file `streamlit_app.py` from CWD `C:\my\path`

### Expected Behavior

The error message `Secrets file not found. Expected at: C:\my\path\.streamlit\secrets.toml` is printed in the streamlit app in an `st.error` alert.

### Current Behavior

The error message `Secrets file not found. Expected at: C:\my\path.streamlit\secrets.toml` (notice the missing path separator between `path` and `.streamlit`) is printed instead

### Is this a regression?

- [ ] Yes, this used to work in a previous version.

### Debug info

- Operating System: Windows

### Additional Information

_No response_

### Are you willing to submit a PR?

- [ ] Yes, I am willing to submit a PR!