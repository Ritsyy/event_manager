from models import Event
from db import session

from flask.ext.restful import reqparse
from flask.ext.restful import abort
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with

event_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'venue': fields.String,
    'organizer': fields.String,
    'registeration_fees': fields.Integer,
    'start_date_time': fields.DateTime(dt_format='rfc822'),
    'end_date_time': fields.DateTime(dt_format='rfc822'),
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('description', type=str)
parser.add_argument('venue', type=str)
parser.add_argument('organizer', type=str)
parser.add_argument('registeration_fees', type=int)
parser.add_argument('start_date_time', type=str)
parser.add_argument('end_date_time', type=str)


class EventsResource(Resource):
    @marshal_with(event_fields)
    def get(self, id):
        event = session.query(Event).filter(Event.id == id).first()
        if not event:
            abort(404, message="Event {} doesn't exist".format(id))
        return event

    def delete(self, id):
        event = session.query(Event).filter(Event.id == id).first()
        if not event:
            abort(404, message="Event {} doesn't exist".format(id))
        session.delete(event)
        session.commit()
        return {}, 204

    @marshal_with(event_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        event = session.query(Event).filter(Event.id == id).first()
        event.name = parsed_args['name']
        event.description = parsed_args['description']
        event.venue = parsed_args['venue']
        event.organizer = parsed_args['organizer']
        event.registeration_fees = parsed_args['registeration_fees']
        event.start_date_time = parsed_args['start_date_time']
        event.end_date_time = parsed_args['end_date_time']
        session.add(event)
        session.commit()
        return event, 201


class EventsListResource(Resource):
    @marshal_with(event_fields)
    def get(self):
        event = session.query(Event).all()
        return event

    @marshal_with(event_fields)
    def post(self):
        parsed_args = parser.parse_args()
        event = Event(name=parsed_args['name'],
                      description=parsed_args['description'],
                      venue=parsed_args['venue'],
                      organizer=parsed_args['organizer'],
                      registeration_fees=parsed_args['registeration_fees'],
                      start_date_time=parsed_args['start_date_time'],
                      end_date_time=parsed_args['end_date_time']
                      )
        session.add(event)
        session.commit()
        return event, 201
