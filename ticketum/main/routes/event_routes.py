from flask import Blueprint
from flask_restful import Api
from main.controllers import EventsResource, EventResource

event_bp = Blueprint('event', __name__)
api = Api(event_bp)

api.add_resource(EventsResource, '/events')
api.add_resource(EventResource, '/events/<int:event_id>')
