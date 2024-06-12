from flask_restful import Resource
from flask import request
from main.services import GuestService
from main.map import GuestSchema
import random

guest_service = GuestService()
guest_schema = GuestSchema()

class GuestsResource(Resource):
    '''
    Class that represents the Guests Resource
    '''
    def post(self):
        json_data = request.get_json()

        # Generate the guest code random with the specific format 'G-XXXX'
        guest_code = 'G-' + str(random.randint(1000, 9999))

        # Add the guest code to the json data
        json_data['guest_code'] = guest_code

        # Deserialize the json data
        data = guest_schema.load(json_data)

        guest = guest_service.create(
            guest_code=guest_code,
            name=data.name,
            email=data.email,
            phone=data.phone,
            dni=data.dni
        )
        return guest_schema.dump(guest), 201

    def get(self):
        guests = guest_service.find_all()
        return guest_schema.dump(guests, many=True), 200
    
class GuestResource(Resource):
    '''
    Class that represents the Guest Resource
    '''
    def get(self, guest_id):
        guest = guest_service.find_by_id(guest_id)
        return guest_schema.dump(guest), 200

    def put(self, guest_id):
        json_data = request.get_json()

        data = guest_schema.load(json_data)
        guest = guest_service.update(
            id=guest_id,
            name=data.name,
            email=data.email,
            phone=data.phone,
            dni=data.dni
        )
        return guest_schema.dump(guest), 200

    def delete(self, guest_id):
        guest_service.delete(guest_id)
        return '', 204
