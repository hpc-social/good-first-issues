---
tags: Style
title: "Standardize on import numpy as np"
html_url: "https://github.com/biopython/biopython/issues/4238"
user: peterjc
repo: biopython/biopython
---

I think we should follow the numpy documentation and avoid the plain ``import numpy`` form in favour of ``import numpy as np``.

With the current code base:

```
$ cat *.py */*.py */*/*.py | grep "import numpy" | sort | uniq -c
   1         >>> import numpy
   9     import numpy
   3     import numpy as np
   1     import numpy as np  # type: ignore
  17 import numpy
   1 import numpy  # type: ignore
   8 import numpy as np
   1 import numpy as np  # type: ignore
   1 import numpy.linalg
```

This is a fairly simple change with search-and-replace (e.g. using ``sed`` at the command line), suitable for a first-time contributor so marking as such.