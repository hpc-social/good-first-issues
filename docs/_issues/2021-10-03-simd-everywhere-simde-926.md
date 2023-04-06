---
tags: ,bug
title: "Problem with _mm256_shuffle_pd"
html_url: "https://github.com/simd-everywhere/simde/issues/926"
user: Kagami
repo: simd-everywhere/simde
---

Hi,

with the following code:

```cpp
#include <stdio.h>
#include <stdint.h>
#include "simde/simde/x86/avx.h"

int main() {
    uint64_t tmp_0[] = {1, 0, 0, 0};
    uint64_t tmp_1[] = {0, 0, 1, 0};
    uint64_t tmp_2[] = {0, 0, 0, 0};

    simde__m256d tmp_0_yd = simde_mm256_loadu_pd((double*)tmp_0);
    simde__m256d tmp_1_yd = simde_mm256_loadu_pd((double*)tmp_1);
    simde__m256d tmp_2_yd = simde_mm256_shuffle_pd(tmp_0_yd, tmp_1_yd, 0b1100);

    simde_mm256_storeu_pd((double*)tmp_2, tmp_2_yd);
    printf("%lu %lu %lu %lu\n", tmp_2[0], tmp_2[1], tmp_2[2], tmp_2[3]);

    return 0;
}
```

compilation with `-mavx` produces:

```
$ g++ -mavx -o 1 1.cpp && ./1
1 0 0 0
```

(as expected). But without that flag the result is:

```
0 0 0 1
```

which is wrong. I suspect there's a problem in emulated version of `_mm256_shuffle_pd`.
I have this problem on NEON machine (m1). On x86 machine with AVX instruction set `-mavx` flag enables native version which works correctly.