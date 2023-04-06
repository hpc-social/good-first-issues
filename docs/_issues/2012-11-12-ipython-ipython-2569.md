---
tags: ,documentation
title: "Add install instructions when dependencies are missing"
html_url: "https://github.com/ipython/ipython/issues/2569"
user: shazow
repo: ipython/ipython
---

Right now:

```
$ ipython notebook
[... snip]
        raise ImportError("%s requires pyzmq >= %s"%(module, minimum_version))
ImportError: IPython.zmq requires pyzmq >= 2.1.4
```

This is not super helpful. More helpful would be to have a message like:

```
$ ipython notebook
You're missing some dependencies required to run the IPython notebook. You can
install them by doing:

    easy_install ipython[zmq,qtconsole,notebook,test]

 Or see read this for more information: http://ipython.org/ipython-doc/dev/install/install.html#installnotebook
```

Bonus points if there was a PyPI metapackage which just pulls in the right dependencies, such as `ipython-notebook`.
