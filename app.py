#!/usr/bin/env python

from flask import Flask
from flask.ext.restful import Api

app = Flask(__name__)
api = Api(app)

from resources import EventsResource
from resources import EventsListResource

api.add_resource(EventsListResource, '/events', endpoint='events')
api.add_resource(EventsResource, '/event/<string:id>', endpoint='event')

if __name__ == '__main__':
    app.run(debug=True)
