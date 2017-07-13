# -*- coding: utf-8 -*-
#
# This file is part of the Bottle Rest Api Prototype.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/Baguage/bottle-rest-api-prototype
#
# This Source Code Form is subject to the terms of the MIT License.
# If a copy of theMIT License was not distributed
# with this file, You can obtain one at https://opensource.org/licenses/MIT
from bottle import get, route, post, request, run, template

@get('/')
def index_get():
    # GET http://localhost:8080/?username=Alex
    username = request.query.get('username', None)
    if username is None:
        return {}

    # Python dictionaries (or subclasses thereof) are automatically transformed into JSON strings and returned
    # to the browser with the Content-Type header set to application/json. This makes it easy to implement
    # json-based APIs.
    return {"Hello": username}

@post('/')
def index_post():
    # POST http://localhost:8080/
    # Assumes POST content in regular form-data format
    username = request.forms.get('username')
    if username is None:
        return {}

    # Python dictionaries (or subclasses thereof) are automatically transformed into JSON strings and returned
    # to the browser with the Content-Type header set to application/json. This makes it easy to implement
    # json-based APIs.
    return {"Hello": username}

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


if __name__ == '__main__':
    run(host='localhost', port=8080)
