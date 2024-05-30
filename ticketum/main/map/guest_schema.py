from marshmallow import Schema, fields, validate, post_load
from main.models import GuestModel

class GuestSchema(Schema):
    '''
    Mapping class to serialize and deserialize the GuestModel
    '''
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Str(required=True)
    phone = fields.Str(validate=validate.Length(max=20))
    dni = fields.Int(required=True)

    inscriptions = fields.List(fields.Nested('InscriptionSchema', exclude=('guest_detail',)))

    # Method to deserialize the data
    @post_load
    def make_guest(self, data, **kwargs):
        return GuestModel(**data)