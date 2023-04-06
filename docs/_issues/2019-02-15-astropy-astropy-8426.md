---
tags: ,Docs,Feature-Request,Hacktoberfest,convolution
title: "convolve_fft defaults and documentation"
html_url: "https://github.com/astropy/astropy/issues/8426"
user: astromark
repo: astropy/astropy
---

I've just been trying to run some code that I haven't used for a year or two, when I had an older version of astropy installed (I'm now running 2.0.10). It was giving very strange results and I eventually managed to track this done to convolve_fft. I found that if I change my `convolve_fft(image,psf)` to `convolve_fft(image,psf,nan_treatment='fill',normalize_kernel=False)` I could then reproduce the results I was getting previously. I take it the defaults were changed at some point, presumably related to #926. Can I suggest that it would make debugging old code much easier if changes that break backwards compatibility, such as this, are noted in the documentation? I'm thinking of something along the lines of http://docs.astropy.org/en/v2.0.x/io/fits/api/files.html#writeto where it clearly states 'Changed in version 1.3: overwrite replaces the deprecated clobber argument.'

The examples also need to be completely rewritten as they were clearly written using the old defaults. For instance, the second one `convolve_fft([1, np.nan, 3], [1, 1, 1])` now gives the result `array([0.5, 2. , 1.5])`.