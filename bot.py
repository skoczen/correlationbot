#!/usr/bin/env python
import functools
import os
import numpy
from bottle import error, Bottle, jinja2_view, request, response 


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
    if not request.headers.get("Content-Type") == "application/json":
        response.content_type = 'application/json'
        response.status = 400
        return "You must post with a Content-Type of application/json."
    else:
        # Validate data is similar to:
        # "data": [
        #     [1, 2, 3, 4],
        #     [5, 6, 7, 8]
        # ]
        if "data" not in request.json:
            response.content_type = 'application/json'
            response.status = 400
            return BADLY_FORMATTED_DATA_ERROR
        else:
            datasets = request.json["data"]
            if not type(datasets) == type([]):
                response.content_type = 'application/json'
                response.status = 400
                return BADLY_FORMATTED_DATA_ERROR
            else:
                if len(datasets) < 2:
                    response.content_type = 'application/json'
                    response.status = 400
                    return "You'll need to provide more than one dataset."
                list_len = None
                for s in datasets:
                    if not list_len:
                        list_len = len(s)
                    else:
                        if list_len != len(s):
                            response.content_type = 'application/json'
                            response.status = 400
                            return "Datasets were of unequal length."
                    for r in s:
                        try:
                            float(r)
                        except:
                            response.content_type = 'application/json'
                            response.status = 400
                            return "Posted data contains a non-number: '%s'" % r


        # Data's all good. run the correlations.
        correlations = []
        all_correlations = numpy.corrcoef(datasets)

        # Actually, do this all at once using numpy
        for col_1_index in range(0, len(datasets)):
            for col_2_index in range(col_1_index, len(datasets)):
                if col_1_index != col_2_index:
                    pearson = all_correlations[col_1_index][col_2_index]
                    
                    # Different column.
                    correlations.append({
                        "column_1": col_1_index+1,
                        "column_2": col_2_index+1,
                        "correlation": pearson,
                        # "covariance": numpy.cov(datasets[col_1_index], datasets[col_2_index]),
                        "pearson": pearson,
                        # "spearman": 0.4,
                        # "kendall": 0.2,
                    })

        data = {"correlations": correlations}
        return data
        


if __name__ == '__main__':
    PORT = os.environ.get("PORT", 80)
    DEBUG = os.environ.get("DEBUG_ON", "false") == "true"
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG, reloader=DEBUG)
