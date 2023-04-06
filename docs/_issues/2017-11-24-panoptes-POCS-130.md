---
tags: ,arduino
title: "Consider reading temperature from CPU, using to control computer box fan"
html_url: "https://github.com/panoptes/POCS/issues/130"
user: jamessynge
repo: panoptes/POCS
---

We have a fan in the computer box, but don't automatically turn it on or off, but we really should make better use of that hardware.

We have temp sensors in the computer box. And the CPU/GPU/motherboard expose temperature sensors (see the Linux package lm-sensors). Any of these might be used to decide when to turn the fan on or off.

Given that not all models of the NUC have fans, and that we have sensors in the case, we might use choose to have two triggers: PEAS could monitor the temperatures in the computer box and of the NUC, and if any of them rise too high it could turn on the fan.

**Edit (@wtgee):**
* [ ] Decide on temperature cutoff limits and add to config.
* [ ] Write a script that checks the temperature and turns the fan off and on accordingly. This script will use the `pustil` module to get the system temperature. For other temperatures you can either:
  * [ ] Listen to zeromq status messages for the `weather` and the `environment` (preferred).
  * [ ] Read the `weather` and `environment` records from the database (actually defaults to flat json files rather than a real database).
* [ ] Run this script as a separate process from within the [PEAS shell](https://github.com/panoptes/POCS/blob/develop/bin/peas_shell).