from marshmallow import Schema, fields, validate, post_load
from main.models import EventModel

class EventSchema(Schema):
    '''
    Mapping class to serialize and deserialize the EventModel
    '''
    id = fields.Int(dump_only=True)
    event_code = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    date = fields.Str(required=True)
    location = fields.Str(required=True)
    capacity = fields.Int(required=True)

    # Method to deserialize the data
    @post_load
    def make_event(self, data, **kwargs):
        return EventModel(**data)