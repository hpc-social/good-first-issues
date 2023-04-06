---
tags: ,doc,types-and-dispatch
title: "Better introduction to parametric types in the manual"
html_url: "https://github.com/JuliaLang/julia/issues/43811"
user: adigitoleo
repo: JuliaLang/julia
---

After a discussion in IRC today I realised that there were a few things about parametric types that aren't easily understood. It seems that the manual could help a bit more in introducing parametric types. I'm opening this issue to outline some of the things I think could be documented better, and also to gather ideas or examples that might help to write a more hands-on parametric types section in the manual. Not sure if this belongs on the forum but I am thinking of linking a PR at some point.

For the parametric type `Foo` and an instance `foo`, I think the docs could clarify
- why both `isabstracttype(Foo)` and `isconcretetype(Foo)` return false for the parametric type `Foo`, i.e. that parametric types are neither abstract nor concrete
- the difference between the following definitions of `Foo`

```julia
struct Foo{T}
    a::T
    b::T
end

struct Foo{T1, T2}
    a::T1
    b::T2
end
```
- why `typeof(foo) <: Foo` is true, however `supertype(typeof(foo)) == Foo` is false (it's `Any`)
- why `Foo isa DataType` is false

and (more visibly) inform
- ~~that parametric types cannot be subtyped~~ they can, parametric abstract types are a thing
- that reified instances of parametric types are of a concrete type, therefore `typeof(foo) != Foo` where `foo` is an instance of `Foo`
- that `foo isa Foo` must be used to test if `foo` is an instance of `Foo`

I also think there should be one example on how to set up a simple but complete type hierarchy (without going into all of the gritty details of the Advanced Types section). Something like the comment by wasshin in #4935.

There might be some other things I've forgotten, feel free to suggest related improvements. I feel that parametric types are one of the major features of Julia's type system, however they can be confusing when coming from languages with more traditional/simple OOP systems. Understanding parametric types should help to reduce common antipatterns like over-constraining argument types, and help people to leverage the dispatch system (what are all those `<:` needed for anyway?)