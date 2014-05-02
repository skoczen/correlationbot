correlationbot
==============

Correlationbot is the simplest way to find insights in data.

# Using Correlationbot

He is one endpoint:

1. Use HTTP on http://correlationbot.com.  `GET` for instructions, `POST` for results.


```python
# TODO: change this to curl.
import requests

requests.POST("http://correlationbot.com", data={
    "data": [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
})

print requests.json
>>> [{
        index1: "1",
        index2: "2",
        correlation: 0.93,
        covariance_1: -0.93,
        pearson: 0.93,
        spearman: 0.4,
        kendall: 0.2,
    },]
```

# Deploying Correlationbot
1. `export PORT=9099` (or have permissions to port 80.)
2. `python bot.py`
