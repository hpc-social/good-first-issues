---
tags: statusawaiting-team-response,typeenhancement
title: "Add a config option to disable warning for setting both a widget default and its key in session_state"
html_url: "https://github.com/streamlit/streamlit/issues/3605"
user: vdonato
repo: streamlit/streamlit
---

We currently print a warning as shown below when a user sets both a widget default value in the function defining the widget as well as a widget value via the widget's key in `st.session_state`

![warning screenshot](https://raw.githubusercontent.com/streamlit/docs/main/public/images/state_value_api_exception.png)

While we certainly want to do this by default since doing both is not recommended, we should provide a config option allowing users to disable the warning in case there's a good reason a user might want to do this.

---

Community voting on feature requests enables the Streamlit team to understand which features are most important to our users.

**If you'd like the Streamlit team to prioritize this feature request, please use the 👍 (thumbs up emoji) reaction in response to the initial post.**