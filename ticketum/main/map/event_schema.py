from marshmallow import Schema, fields, validate, post_load
from main.models import EventModel

class EventSchema(Schema):
    '''
    Mapping class to serialize and deserialize the EventModel
    '''
    code = fields.Str(attribute='event_code', required=True, validate=validate.Length(min=1, max=100))
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    date = fields.Str(required=True)
    location = fields.Str(required=True)
    capacity = fields.Int(required=True)

    inscriptions = fields.List(fields.Nested('InscriptionSchema', exclude=('event',)))

    total_inscriptions = fields.Method("get_total_inscriptions")

    def get_total_inscriptions(self, event):
        return len(event.inscriptions)

    # Method to deserialize the data
    @post_load
    def make_event(self, data, **kwargs):
        return EventModel(**data)