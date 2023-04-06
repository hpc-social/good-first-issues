---
tags: ,bug-lady_beetle
title: "Widgets code shows up during the commandline "
html_url: "https://github.com/tardis-sn/tardis/issues/1976"
user: wkerzendorf
repo: tardis-sn/tardis
---

It should be disabled when running on the commandline. 
```
VBox(children=(FigureWidget({█▏                                                            119918/500000 [00:12<00:38, 9986
    'data': [{'type': 'scatter', 'uid': 'a781058b-c248-4e8b-a41f-c9232fc3fe15', 'xaxis': 'x', 'yaxis': 'y'},
             {'type': 'scatter', 'uid': '1bed6058-4acd-4c65-b2e0-cd0062fc8e29', 'xaxis': 'x2', 'yaxis': 'y2'}],
    'layout': {'height': 450,
               'legend': {'title': {'text': 'Iterations'}, 'traceorder': 'reversed'},
               'margin': {'b': 25, 'l': 10, 'pad': 0, 'r': 135, 't': 25},
               'template': '...',
               'xaxis': {'anchor': 'y',
                         'domain': [0.0, 0.45],
                         'tickformat': 'g',
                         'title': {'text': '$\\text{Velocity}~[\\text{km}~\\text{s}^{-1}]$'}},
               'xaxis2': {'anchor': 'y2',
                          'domain': [0.55, 1.0],
                          'matches': 'x',
                          'tickformat': 'g',
                          'title': {'text': '$\\text{Velocity}~[\\text{km}~\\text{s}^{-1}]$'}},
               'yaxis': {'anchor': 'x',
                         'domain': [0.0, 1.0],
                         'nticks': 15,
                         'tickformat': 'g',
                         'title': {'text': '$T_{\\text{rad}}\\ [\\text{K}]$'}},
               'yaxis2': {'anchor': 'x2',
                          'domain': [0.0, 1.0],
                          'nticks': 15,
                          'tickformat': 'g',
                          'title': {'text': '$W$'}}}
```