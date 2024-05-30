from marshmallow import Schema, fields, validate, post_load
from main.models import InscriptionModel

class InscriptionSchema(Schema):
    '''
    Mapping class to serialize and deserialize the InscriptionModel
    '''
    id = fields.Int(dump_only=True)
    status = fields.Str(required=True)
    event_id = fields.Int(required=True)
    guest_id = fields.Int(required=True)

    event = fields.Nested('EventSchema', exclude=('inscriptions_details',))
    guest = fields.Nested('GuestSchema', exclude=('inscriptions_details',))

    # Method to deserialize the data
    @post_load
    def make_inscription(self, data, **kwargs):
        return InscriptionModel(**data)