from flask_restful import Resource
from flask import request
from main.services import EventService
from main.map import EventSchema
from datetime import datetime

event_service = EventService()
event_schema = EventSchema()

class EventsResource(Resource):
    '''
    Class that represents the Events Resource
    '''
    def post(self):
        json_data = request.get_json()

        # Set the actual datetime if the date is not provided
        if 'date' not in json_data:
            json_data['date'] = datetime.now()

        # Set the date to string type
        json_data['date'] = json_data['date'].strftime('%Y-%m-%d %H:%M:%S')

        data = event_schema.load(json_data)
        
        # Create an event using the deserialized object directly
        event = event_service.create(
            event_code=data.event_code,
            name=data.name,
            description=data.description,
            date=data.date,
            location=data.location,
            capacity=data.capacity
        )
        return event_schema.dump(event), 201

    def get(self):
        events = event_service.find_all()
        return event_schema.dump(events, many=True), 200

class EventResource(Resource):
    '''
    Class that represents the Event Resource
    '''
    def get(self, event_id):
        event = event_service.find_by_id(event_id)
        return event_schema.dump(event), 200

    def put(self, event_id):
        json_data = request.get_json()
        data = event_schema.load(json_data)
        
        event = event_service.update(
            id=event_id,
            event_code=data.event_code,
            name=data.name,
            description=data.description,
            date=data.date,
            location=data.location,
            capacity=data.capacity
        )
        return event_schema.dump(event), 200

    def delete(self, event_id):
        event_service.delete(event_id)
        return '', 204
