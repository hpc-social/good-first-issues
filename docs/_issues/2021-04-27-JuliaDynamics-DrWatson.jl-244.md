---
tags: low-priority,saving-files
title: "`tag!()` always includes name of the last git tag with a message"
html_url: "https://github.com/JuliaDynamics/DrWatson.jl/issues/244"
user: imLew
repo: JuliaDynamics/DrWatson.jl
---

The `!tag(d)` function typically adds the hash of the current commit to the dictionary `d` even if there is a tag at the current commit.
But if any commit has a tag with a message `tag!()` will use the name of the tag+numbers of commits since the tag+7 symbols of current commit hash for the value of `:gitcommit`. It seems to always use the most recent git tag that was created with a message.

Not sure how to create a runnable MWE for this but with the following commands it should be reproducible in REPL.
```
julia> using DrWatson

julia> initialize_project("project")

shell> cd project/

shell> git tag one

julia> tag!(Dict())
Dict{Any, Any} with 2 entries:
  "gitcommit" => "00552ebdb2ec2a57c1b96e067c1d1b78ef90349b"
  "gitpatch"  => ""

shell> git tag two -m "message"

julia> tag!(Dict())
Dict{Any, Any} with 2 entries:
  "gitcommit" => "two"
  "gitpatch"  => ""

shell> touch file

shell> git add file

shell> git commit -m "message"

julia> tag!(Dict())
Dict{Any, Any} with 2 entries:
  "gitcommit" => "two-1-g045b205"
  "gitpatch"  => ""
```

(Not sure if relevant but I do not seem to have `Agents` installed `julia> Pkg.status("Agents"); #No Matches`)