from flask import Blueprint
from flask_restful import Api
from main.controllers import GuestsResource, GuestResource

guest_bp = Blueprint('guest', __name__)
api = Api(guest_bp)

api.add_resource(GuestsResource, '/guests')
api.add_resource(GuestResource, '/guests/<int:guest_id>')
