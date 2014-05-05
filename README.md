correlationbot
==============

Correlationbot is the simplest way to find insights in data.

# Using Correlationbot

He is one endpoint:

1. Use HTTP on http://correlationbot.com.  `GET` for instructions, `POST` for results.

Curl:

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"data": [[1,2,3,4,6,7,8,9],[2,4,6,8,10,12,13,15]]}' http://correlationbot.com
{"correlations": [{"pearson": 0.99535001355530017, "column_2": 2, "column_1": 1, "correlation": 0.99535001355530017}]}
```

Python:
```python
>>> import json
>>> import requests
>>> headers = {'Content-type': 'application/json', }
>>> resp = requests.post("http://correlationbot.com", headers=headers, data=json.dumps({
    "data": [
        [1, 2, 3],
        [412, 5, 6],
        [45, -125, 6.334],
        # Or any number of equally-sized columns.
    ]
})
>>> print resp.json()
{
    "correlations": [
        {
            "column_1": 1,
            "column_2": 2,
            "correlation": -0.86495821895559954,
            "pearson": -0.86495821895559954,
        },
        {
            "column_1": 1,
            "column_2": 3,
            "correlation": -0.21695628247970969,
            "pearson": -0.21695628247970969,
        },
        {
            "column_1": 2,
            "column_2": 3,
            "correlation": 0.67754874098457696,
            "pearson": 0.67754874098457696,
        }
    ]
]
```


# Deploying Correlationbot
1. `export PORT=9099` (or have permissions to port 80.)
2. `python bot.py`
