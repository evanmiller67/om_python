#/usr/bin/env python3 
"""
title: deco-flask-deco-example.py
author: exm5840
date(created): 2019-09-24 11:59:15 EDT
date (updated): 2019-09-24 11:59:15 EDT
"""

# One of the most used decorators in Python is the login_required() decorator, which ensures that a user is logged in/properly authenticated before s/he can access a specific route (/secret, in this case):

from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass

#deco-flask-dec-example.py-----------------------------------------------

# Example using flask (place in another file...)
#app.py
from flask import Flask, request, abort
from functools import wraps

app = Flask(__name__)


# Below we ensure that the key student_id is part of the request. Although this validation works it really does not belong in the function itself. Plus, perhaps there are other routes that use the exact same validation. So, let’s keep it DRY and abstract out any unnecessary logic with a decorator.
def validate_json(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@app.route('/grade', methods=['POST'])
@validate_json('student_id')
def update_grade():
    json_data = request.get_json()
    print(json_data)
    # update database
    return "success!"


if __name__ == '__main__':
    app.run()
#/app.py-----------------------------------------------------------------
# Run app.py
# $ py app.py
# Curl...
# $ curl -H "Content-Type:application/json" -X POST -d '{"student_id":1}' http://localhost:5000/grade

