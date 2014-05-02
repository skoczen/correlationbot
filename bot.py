#!/usr/bin/env python
import functools
import os
from bottle import abort, Bottle, jinja2_view, request, response 


view = functools.partial(jinja2_view, template_lookup=['templates'])
app = Bottle()

@app.get('/')
@view('home.html')
def instructions():
    return {}


BADLY_FORMATTED_DATA_ERROR = """Data format wasn't correct. Correlationbot expects a JSON post of datasets that looks like:
{
    "data": [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
}
"""

@app.post('/')
def do_correlation():
    if request.headers.get("Content-Type") == "application/json":
        # Validate data is similar to:
        # "data": [
        #     [1, 2, 3, 4],
        #     [5, 6, 7, 8]
        # ]
        if "data" not in request.json:
            abort(400, BADLY_FORMATTED_DATA_ERROR)
        else:
            datasets = request.json["data"]
            if not type(datasets) == type([]):
                abort(400, BADLY_FORMATTED_DATA_ERROR)
            else:
                if len(datasets) < 2:
                    abort(400, "You'll need to provide more than one dataset.")
                list_len = None
                for s in datasets:
                    if not list_len:
                        list_len = len(s)
                    else:
                        if list_len != len(s):
                            abort(400, "Datasets were of unequal length.")
                    for r in s:
                        try:
                            float(r)
                        except:
                            abort(400, "Posted data contains a non-number: '%s'" % r)


        # Data's all good. run the correlations.


        data = {
            "correlations": [
                {
                    index1: "1",
                    index2: "2",
                    correlation: 0.93,
                    covariance_1: -0.93,
                    pearson: 0.93,
                    spearman: 0.4,
                    kendall: 0.2,
                },
            ]
        }
        return data
    else:
        abort(400, "You must post with a Content-Type of application/json.")


if __name__ == '__main__':
    PORT = os.environ.get("PORT", 80)
    DEBUG = os.environ.get("DEBUG_ON", "false") == "true"
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
