---
tags: Docker,feat/enhancement,needs-triage
title: "Create a non-root default user with id 1000"
html_url: "https://github.com/scikit-hep/pyhf/issues/2133"
user: matthewfeickert
repo: scikit-hep/pyhf
---

### Summary

The default user for the `pyhf` images is `root`.

```console
$ docker run --rm -ti --entrypoint /bin/bash pyhf/pyhf:v0.7.0
root@c2f8d937ca29:/# id
uid=0(root) gid=0(root) groups=0(root)
```

This isn't great, as it means that if a user bind mounts their local file system any files they write out will be created as `root` and they will need `sudo` permissions to remove them.

```console
$ docker run --rm -ti -v $PWD:/example --entrypoint /bin/bash pyhf/pyhf:v0.7.0
root@0164cb9f3c8c:~# touch /example/here.txt
root@0164cb9f3c8c:~# ls -l /example/here.txt 
-rw-r--r-- 1 root root 0 Mar 11 22:40 /example/here.txt
root@0164cb9f3c8c:~# exit
exit
$ ls -l here.txt 
-rw-r--r-- 1 root root 0 Mar 11 16:40 here.txt
```

It is perferable to have a default user that is `id` `1000`

```console
$ docker run --rm -ti --user 1000:1000 -v $PWD:/example --entrypoint /bin/bash pyhf/pyhf:v0.7.0
I have no name!@e85dad7d317d:/$ touch /example/here-id1000.txt
I have no name!@e85dad7d317d:/$ ls -l /example/here-id1000.txt 
-rw-r--r-- 1 1000 1000 0 Mar 11 22:42 /example/here-id1000.txt
I have no name!@e85dad7d317d:/$ exit
exit
$ ls -l here-id1000.txt 
-rw-r--r-- 1 feickert feickert 0 Mar 11 16:42 here-id1000.txt
```

### Additional Information

_No response_

### Code of Conduct

- [X] I agree to follow the Code of Conduct