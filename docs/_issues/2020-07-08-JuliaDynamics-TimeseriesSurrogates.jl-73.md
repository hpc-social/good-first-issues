---
tags: ,enhancement
title: "Utility request: preprocessing step of Lancaster et al."
html_url: "https://github.com/JuliaDynamics/TimeseriesSurrogates.jl/issues/73"
user: Datseris
repo: JuliaDynamics/TimeseriesSurrogates.jl
---

The review by Lancaster suggests that when using any Fourier-based surrogates the following preprocessing steps should be made:

1. Remove any trends in the data which are not important or relevant to the results, so that they are not incorporated into the surrogates.
2. Correct any mismatch between start and end points and corresponding first derivatives. This is very important and must not be overlooked, and arises from the assumptions made when calculating any of the Fourier transform based surrogates.
3. Subtract the mean to ensure that results are not affected by significantly different mean values. The

They describe an automated process to ensure this:

![image](https://user-images.githubusercontent.com/19669089/86977648-64891680-c17d-11ea-9bfd-9c2eca303052.png)

We should implement this and offer it as a utility function.