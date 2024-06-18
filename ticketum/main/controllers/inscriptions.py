from flask_restful import Resource
from flask import request
from main.services import InscriptionService, GuestService, EventService
from main.map import InscriptionSchema, GuestSchema, EventSchema
import random

inscription_service = InscriptionService()
inscription_schema = InscriptionSchema()
guest_service = GuestService()
guest_schema = GuestSchema()
event_service = EventService()
event_schema = EventSchema()

'''
Inscription Resources according to the API Contract
'''

class InscriptionsResource(Resource):
    '''
    Class that represents the Inscriptions Resource
    '''
    def post(self, event_code):
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

        # Find the event by the event code
        event = event_service.find_by_code(event_code)
        
        # Create the inscription with the guest created
        inscription_creation = inscription_service.create(
            status='PENDING',
            event_id=event.id,
            guest_id=guest.id
        )

        # Serialize the inscription created
        inscription = inscription_schema.dump(inscription_creation)

        # Return the Inscription created with status, event code and guest code
        inscription_response = {
            'status': inscription['status'],
            'event_code': event.event_code,
            'guest_code': guest_code
        }

        return inscription_response, 200
    
class InscriptionResource(Resource):
    '''
    Class that represents the Inscription Resource
    '''
    def get(self, event_code, guest_code):
        # Find the inscription by the event code and guest code
        inscription = inscription_service.find_by_event_guest_code(event_code, guest_code)

        if not inscription:
            return {'message': 'Inscription not found'}, 404

        # Serialize the inscription found
        inscription_data = inscription_schema.dump(inscription)

        # Return the Inscription found with status, event code, and guest code
        inscription_response = {
            'status': inscription_data['status'],
            'event_code': inscription.event.event_code,
            'guest_code': inscription.guest.guest_code
        }
        return inscription_response, 200

    def delete(self, event_code, guest_code):
        # Find the inscription by the event code and guest code
        inscription_selected = inscription_service.find_by_event_guest_code(event_code, guest_code)
               
        # Update the status of the inscription to 'CANCELLED'
        inscription_service.update(
            id=inscription_selected.id,
            status='CANCELLED',
            event_id=inscription_selected.event_id,
            guest_id=inscription_selected.guest_id
        )
        return "Inscription cancelled", 200