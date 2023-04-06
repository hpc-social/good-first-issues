---
tags: bug
title: "Importing Keras when loading dataset "
html_url: "https://github.com/mirapy-org/mirapy/issues/29"
user: swapsha96
repo: mirapy-org/mirapy
---

I just observed that when I am using any function from `mirapy.data.load_dataset`, the module always runs `from keras.utils.np_utils import to_categorical` which is only used in one function. So if a user just wants to load dataset and doesn't have keras installed, it will throw an error. This is a utility that needs to be replaced by either creating our own `to_categorical` function or find a better way.

*Note:* Once the assignee creates the PR, s/he needs to check if notebook on X-ray binaries is working correctly.