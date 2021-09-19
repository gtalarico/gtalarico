+++
title = "RevitPythonWrapper"
description = "A Python Wrapper For the Revit API"
slug = "revitpythonwrapper"
date = "2017-01-01"
tags = [
    "python",
    "ironpython",
    "revit api",
    "pyrevit",
]
categories = [

]
+++


Revit Python Wrapper was created to help Python programmers write Revit API code.
Wrapper classes make the interaction with API objects less repetitive, and more consistent with Python’s conventions.

<a class="github-button" href="https://github.com/gtalarico/revitpythonwrapper" data-size="large" data-show-count="true" aria-label="Star gtalarico/revitpythonwrapper on GitHub">Star</a>

#### Links

<div class="links">
    <i class="fab fa-github"></i>
    <a href="https://github.com/gtalarico/revitpythonwrapper">Repo</a>
    <br>
    <i class="fas fa-book-open"></i>
    <a href="https://revitpythonwrapper.readthedocs.io/en/latest/">Documentation</a>
</div>

#### Media

![project-logo](https://revitpythonwrapper.readthedocs.io/en/latest/_images/logo-tight.png)

#### Usage
```python
from rpw import revit, db, ui, DB, UI

# Collector Wrapper
doors = db.Collector(of_category='Doors')

# Transaction Wrapper
with db.Transaction('Delete'):
    [revit.doc.Delete(door.id) for door in doors]

# Curves
line = Line.new([-10,0], [10,0])
line.create_detail()

# Parameter Wrapper
wall = db.Element(SomeElementId)
# wall = <rpw: WallInstance % DB.Wall >
wall.parameters['Height']
# 10.0
>>> wall.parameters.builtins['WALL_LOCATION_LINE']
# 1
```




