+++
title = "pyAirtable"
description = "Python Client for Airtable Api"
slug = "airtable"
date = "2017-08-03"
tags = [
    "python",
    "cli",
    "client",
]
categories = [
    "python",
    "cli",
    "client",
    "Open Source",
]
+++

A Python client library for the [Airtable Api](https://airtable.com/api)

#### Links

![repo](https://img.shields.io/github/stars/gtalarico/pyairtable?style=flat-square)\
![docs](https://img.shields.io/readthedocs/pyairtable?style=flat-square)\
![PyPI](https://img.shields.io/pypi/v/pyairtable?style=flat-square)\
![downloads](https://img.shields.io/pypi/dm/pyairtable?style=flat-square&label=downloads%201.x)\
![downloads](https://img.shields.io/pypi/dm/airtable-python-wrapper?style=flat-square&label=downloads%200.x)


#### Usage

```python
from airtable import Airtable
table = Airtable('basekey', 'table_name')

# Get
table.get_all()
# [{id:'rec123asa23', fields': {'Column': 'Value'}, ...}]

# Search
airtable.search('ColumnA', 'SearchValue')
# [{id:'rec123asa23', fields': {'Column': 'Value'}, ...}]
```






