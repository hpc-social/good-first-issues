---
tags: feature,help-wanted,parallel
title: "Distributed.jl should verify Julia version between primary-worker"
html_url: "https://github.com/JuliaLang/julia/issues/45362"
user: daharn
repo: JuliaLang/julia
---

As described already [here](https://discourse.julialang.org/t/fetch-from-remote-machine-produces-typeerror-non-boolean-nothing-used-in-boolean-context-for-differing-julia-versions/81271), running

```julia
using Distributed
addprocs(["<remotename>"], exename="<pathToRemoteJuliaExe>", dir="<pathToRemoteHomeDir>")

@fetch myid()
```

on a host with Julia 1.6.1 and connecting to a remote with Julia 1.7.2 leads to 

```julia
ERROR: On worker 2:
TypeError: non-boolean (Nothing) used in boolean context
Stacktrace:
  [1] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:1166
  [2] handle_deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:947
  [3] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:801 [inlined]
  [4] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:1018
  [5] handle_deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:947
  [6] deserialize_fillarray!
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:1230
  [7] deserialize_array
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:1222
  [8] handle_deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:852
  [9] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:801 [inlined]
 [10] deserialize_typename
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:1296
 [11] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Distributed/src/clusterserialize.jl:68
 [12] handle_deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:947
 [13] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:801
 [14] handle_deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:858
 [15] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:801
 [16] handle_deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:861
 [17] deserialize
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Serialization/src/Serialization.jl:801 [inlined]
 [18] deserialize_msg
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Distributed/src/messages.jl:87
 [19] #invokelatest#2
    @ ./essentials.jl:716 [inlined]
 [20] invokelatest
    @ ./essentials.jl:714 [inlined]
 [21] message_handler_loop
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Distributed/src/process_messages.jl:169
 [22] process_tcp_streams
    @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.7/Distributed/src/process_messages.jl:126
 [23] #99
    @ ./task.jl:423
Stacktrace:
 [1] #remotecall_fetch#143
   @ /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.6/Distributed/src/remotecall.jl:394 [inlined]
 [2] remotecall_fetch(::Function, ::Distributed.Worker)
   @ Distributed /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.6/Distributed/src/remotecall.jl:386
 [3] remotecall_fetch(::Function, ::Int64; kwargs::Base.Iterators.Pairs{Union{}, Union{}, Tuple{}, NamedTuple{(), Tuple{}}})
   @ Distributed /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.6/Distributed/src/remotecall.jl:421
 [4] remotecall_fetch(::Function, ::Int64)
   @ Distributed /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.6/Distributed/src/remotecall.jl:421
 [5] top-level scope
   @ none:1
```

However, when I use Julia 1.7.2 instead of 1.6.1 on the host, everything works as expected. Both systems run CentOS 7.
