---
tags: c-core,c-methods,help-wanted,s-keep-open,t-feature-request
title: "Standardize error handling"
html_url: "https://github.com/mlpack/mlpack/issues/891"
user: rcurtin
repo: mlpack/mlpack
---

A long time ago, the general rule of thumb (at least that I used) was to use `Log::Fatal` to handle errors, but sometimes e.g. `Log::Debug` was used to just print the error instead and continue going.  But in other places, sometimes exceptions are being thrown (and `Log::Fatal` itself will throw an exception when a newline is encountered).

One of the most frustrating things about using a new library or tool is when it doesn't give good or consistent error handling output, so we should work to ensure that all of mlpack's output is consistent and easy to handle.  We have some nice pieces:

 * A logging system
 * A backtrace system (only available on Linux at the moment though and only in debugging mode)
 * The C++ exception infrastructure

So how should we make something that makes mlpack easy to debug?  Ideally, if a user gets an error, they should be able to quickly understand what went wrong (usually the error will probably be with their data) and maybe get some guidance on how it might be fixed, such as in the situation where the data has invalid entries, or some guidance on what to learn about to debug further, such as in the situation where some algorithm doesn't converge.

For this issue, before we close it, we should converge on some idea of what we should do, then ensure that all of the error messages in mlpack are consistent.  My current idea (which may not be the best idea!) is that we could return an exception that inherits from `std::exception` with a string field containing the backtrace and the explanation, or something like this.  I think we can also modify the backtrace code so that it works even without debugging symbols---it just doesn't have line numbers.  Using that idea instead of `Log::Fatal` offers the advantage that we can be more clear about the error using the type of the exception---`Log::Fatal` only throws `std::runtime_error`.

This is an open-ended ticket, so it is definitely open for discussion.  I've labeled the difficulty "easy", but by this I only mean that it's going to be implementationally easy, not that coming up with the right idea will be easy. :)