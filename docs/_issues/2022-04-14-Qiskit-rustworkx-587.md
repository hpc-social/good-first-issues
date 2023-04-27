---
tags: enhancement
title: "Expand retworkx-core testing"
html_url: "https://github.com/Qiskit/rustworkx/issues/587"
user: mtreinish
repo: Qiskit/rustworkx
---

<!-- ⚠️ If you do not respect this template, your issue will be closed -->
<!-- ⚠️ Make sure to browse the opened and closed issues to confirm this idea does not exist. -->

### What is the expected enhancement?

Right now most of our testing for `retworkx-core` is done via doc tests and via the retworkx crate's use of it. We do get a fair amount of coverage from these but since the library is designed for rust consumption it'd be good to have some dedicated tests in the retworkx-core crate for testing the specifics of the consumption of the library from rust that go into more depth than what the doc tests cover.