---
tags: areaux/ui,featurest.image,statusconfirmed,typebug
title: "SVG image from e2e tests does not render in Firefox"
html_url: "https://github.com/streamlit/streamlit/issues/5674"
user: AnOctopus
repo: streamlit/streamlit
---

### Checklist

- [X] I have searched the [existing issues](https://github.com/streamlit/streamlit/issues) for similar issues.
- [X] I added a very descriptive title to this issue.
- [X] I have provided sufficient information below to help reproduce this issue.

### Summary

The `st.image` cypress test renders an svg with a github avatar. The avatar appears as expected in chromium, but does not appear in firefox 100. 

### Reproducible Code Example

```Python
import streamlit as st

st.image(
    """<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100" height="100">
    <clipPath id="clipCircle">
        <circle r="25" cx="25" cy="25"/>
    </clipPath>
    <image href="https://avatars.githubusercontent.com/karriebear" width="50" height="50" clip-path="url(#clipCircle)"/>
</svg>
"""
)
```


### Steps To Reproduce

_No response_

### Expected Behavior

Avatar renders in all supported browsers

### Current Behavior

Avatar renders in Chromium, but not Firefox

### Is this a regression?

- [ ] Yes, this used to work in a previous version.

### Debug info

- Operating System: Fedora 34
- Browser: Firefox 100.0.2
- Virtual environment: Pipenv


### Additional Information

_No response_

### Are you willing to submit a PR?

- [X] Yes, I am willing to submit a PR!