from flask_restful import Resource
from flask import request
from main.services import InscriptionService
from main.map import InscriptionSchema

inscription_service = InscriptionService()
inscription_schema = InscriptionSchema()

class InscriptionsResource(Resource):
    '''
    Class that represents the Inscriptions Resource
    '''
    def post(self):
        json_data = request.get_json()
        data = inscription_schema.load(json_data)
        inscription = inscription_service.create(**data)
        return inscription_schema.dump(inscription)

    def get(self):
        inscriptions = inscription_service.find_all()
        return inscription_schema.dump(inscriptions, many=True)
    
class InscriptionResource(Resource):
    '''
    Class that represents the Inscription Resource
    '''
    def get(self, inscription_id):
        inscription = inscription_service.find_by_id(inscription_id)
        return inscription_schema.dump(inscription)

    def put(self, inscription_id):
        json_data = request.get_json()
        data = inscription_schema.load(json_data)
        inscription = inscription_service.update(inscription_id, **data)
        return inscription_schema.dump(inscription)

    def delete(self, inscription_id):
        inscription = inscription_service.delete(inscription_id)
        return inscription_schema.dump(inscription)