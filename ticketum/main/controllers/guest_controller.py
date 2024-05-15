from flask_restful import Resource
from flask import request
from main.services import GuestService
from main.map import GuestSchema

guest_service = GuestService()
guest_schema = GuestSchema()

class GuestsResource(Resource):
    '''
    Class that represents the Guests Resource
    '''
    def post(self):
        json_data = request.get_json()
        data = guest_schema.load(json_data)
        guest = guest_service.create(**data)
        return guest_schema.dump(guest)

    def get(self):
        guests = guest_service.find_all()
        return guest_schema.dump(guests, many=True)
    
class GuestResource(Resource):
    '''
    Class that represents the Guest Resource
    '''
    def get(self, guest_id):
        guest = guest_service.find_by_id(guest_id)
        return guest_schema.dump(guest)

    def put(self, guest_id):
        json_data = request.get_json()
        data = guest_schema.load(json_data)
        guest = guest_service.update(guest_id, **data)
        return guest_schema.dump(guest)

    def delete(self, guest_id):
        guest = guest_service.delete(guest_id)
        return guest_schema.dump(guest)