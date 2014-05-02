import functools
import os
from bottle import Bottle, request, jinja2_view


view = functools.partial(jinja2_view, template_lookup=['templates'])
app = Bottle()

@app.get('/')
@view('home.html')
def instructions():
    return {}


@app.post('/')
def do_correlation():
    data = request.json
    print data
    return "Here's your data!"


if __name__ == '__main__':
    PORT = os.environ.get("PORT", 80)
    DEBUG = os.environ.get("DEBUG_ON", False)
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
