---
tags: enhancement
title: "Support different audio / directory structures"
html_url: "https://github.com/CouncilDataProject/speakerbox/issues/18"
user: evamaxfield
repo: CouncilDataProject/speakerbox
---

<!--
  ⚠️⚠️ Please do the following before submitting: ⚠️⚠️

  📖 Please read our Code of Conduct.
  🔎 Please search existing issues to avoid creating duplicates.
-->

### Feature Description

<!-- A clear and concise description of the feature you're requesting. -->

Support a more direct directory structure of speakers instead of "conversations". i.e.:

```
data/
├── bob/
|   ├── 0.wav
|   ├── 1.wav
|   ├── 2.wav
|   ├── 3.wav
|   ├── 4.wav
├── sally/
|   ├── 5.wav
|   ├── 6.wav
|   ├── 7.wav
|   ├── 8.wav
|   ├── 9.wav
└── eva/
    ├── 10.wav
    ├── 11.wav
    ├── 12.wav
    ├── 13.wav
    ├── 14.wav
```

Where all the audio for each speaker is provided as a directory. This would involve creating new functions for preparing the dataset -- with no guarantee that the "conversation id" holdout condition is met.

### Use Case

<!-- Please provide a use case to help us understand your request in context. -->

See #17 -- direct use case already done.

### Solution

<!-- Please describe your ideal solution. -->

### Alternatives

<!-- Please describe any alternatives you've considered, even if you've dismissed them. -->

