---
tags: ,help-wanted,tfeat
title: "rendering a single/monolithic offlineable html file"
html_url: "https://github.com/nextstrain/nextclade/issues/283"
user: dpark01
repo: nextstrain/nextclade
---

Hi @ivan-aksamentov, question about nextclade (and as always, thanks for this great work)

For context, my questions are primarily around trying to figure out how to incorporate it into a workflow-based compute system, where people's data are analyzed asynchronously and results returned to them for examination. Which is why I asked earlier about being able to pre-compute the parts of nextclade that actually involve computing anything, and having the user only have to deal with rendering (ie, if the node/react webapp could just take the cli json output and just focus on rendering it)
An even further ideal is exemplified by a tool I always point to, krona (https://github.com/marbl/Krona/wiki/KronaTools), which is a CLI tool that takes input data and produces a single, all-in-one html file (js and css all embedded in-line -- no references to anything on the internet). The user can then view that html file in their browser whether online or offline, and get the full interactive js UI with the visualizations--at no point is a server (web server, node web app) required. Makes it super simple to incorporate the tool into a file-based workflow compute environment.

Personally I don't know my node/react well enough to know how to contribute in such a way, but even if it's as dumb as writing a script that spins up nextclade via yarn in a docker image and then uses wget to push inputs and pull outputs to an html file, then collects all the referenced css/js assets and somehow embeds them within, that ought to do the trick in theory... googling around seems to imply that it might be even easier than that depending on what frameworks were used under the hood (https://stackoverflow.com/questions/51949719/is-there-a-way-to-build-a-react-app-in-a-single-html-file)

Anyway, this is more of a pre-exploratory question than asking for a specific feature request at the moment. I'm more curious based on your sense of it whether you think this is a significant amount of effort or whether it's possibly straightforward if someone had time and was motivated. Looking at the documentation on nextclade, which says "These sequences will then be analyzed in your browser -- data never leave your computer", this makes me think that this should be pretty feasible--there's no server-side processing happening currently, so we shouldn't need a server.. react code should be something that could be embedded in a static/offline html in theory.

Curious to know what you think!