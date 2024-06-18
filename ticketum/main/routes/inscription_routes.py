from flask import Blueprint
from flask_restful import Api
from main.controllers import InscriptionsResource, InscriptionResource

inscription_bp = Blueprint('inscription', __name__)
api = Api(inscription_bp)

api.add_resource(InscriptionsResource, '/events/<string:event_code>/inscriptions')
api.add_resource(InscriptionResource, '/events/<string:event_code>/inscriptions/<string:guest_code>')
