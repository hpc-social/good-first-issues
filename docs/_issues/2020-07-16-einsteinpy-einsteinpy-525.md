---
tags: ,coordinates,enhancement,metric,new-feature,research
title: "Add new coordinate and metric classes"
html_url: "https://github.com/einsteinpy/einsteinpy/issues/525"
user: JeS24
repo: einsteinpy/einsteinpy
---

<!--

WELCOME ABOARD!

Hi and welcome to the einsteinpy project. We appreciate bug reports, questions
about documentation, and suggestions for new features.

IMPORTANT: If you are reporting a problem with einsteinpy, please follow the
template below. If it's a suggestion, a possible new addition to the library,
or just want to say "Thank you!", you can remove all this text and start
from scratch.

-->
<!--- Provide a general summary of the issue in the Title above -->

🐞 **What bugs you?**

The core modules of EinsteinPy are well-integrated, after #512 & #521. Now, we can add more metric classes to the module, in all usual coordinates, corresponding to the metric. This will be an ongoing issue, tracking new coordinate and metric additions, quite similar to the issue for symbolic module (#309). Related issues are #15 and #16.

🎯 **Goal**

<!--- Why is this change important to you? How would you use it? -->
<!--- How can it benefit other users? -->
Add new metric and coordinate classes to enhance the numerical relativity toolkit, offered by EinsteinPy. An important addition would be a class for Kerr-Schild Coordinates in `einsteinpy.coordinates` and Kerr-Schild forms of the vacuum solutions (`Schwarzschild`, `Kerr` and `KerrNewman` classes, as of now) in `einsteinpy.metric`.

💡 **Possible solutions**

<!--- Not obligatory, but suggest an idea for implementing addition or change -->
https://arxiv.org/pdf/0904.4184.pdf is a good source for many metric classes, along with their corresponding coordinates. More resource suggestions are welcome.

📋  **Steps to solve the problem**

 * Comment below, which metric or coordinate, you've started working on.
 * Add, commit, push your changes.
 * Submit a pull request and add this in comments - `Addresses #<put issue number here> | Adds support for <put metric or coordinate name here>`.
 * Ask for a review in comments section of pull request.
 * Celebrate your contribution to this project 🎉
