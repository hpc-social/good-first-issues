---
tags: ,enhancement
title: "make model runs end at the time specified."
html_url: "https://github.com/DeltaRCM/pyDeltaRCM/issues/115"
user: amoodie
repo: DeltaRCM/pyDeltaRCM
---

Currently, model runs specified with the `time` input to the high-level api do not end at the exact specified time. They get close, but it is inexact because the timestep is not necessarily a factor of the specified end time. One way to address this:

Just before entering the iteration-updating-while-loop, take the model calculated `dt = deltamodel.dt` and do `whole = endtime // dt`  and `rem = endtime % dt`, then just set up a loop that runs `whole` times, and then a single update that sets `deltamodel.dt = rem / deltamodel.dt` and then runs one final `deltamodel.update()`.
