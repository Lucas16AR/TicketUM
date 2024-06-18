from flask_restful import Resource
from flask import request
from main.services import EventService
from main.map import EventSchema
from datetime import datetime

event_service = EventService()
event_schema = EventSchema()

'''
Event Resources according to the API Contract
'''

class EventsResource(Resource):
    '''
    Class that represents the Events Resource
    '''

    def get(self):
        # Find all the events
        events = event_service.find_all()
        
        # Prepare a list to store modified event data
        modified_events = []

        for event in events:
            # Dump the event data without inscriptions
            event_data = event_schema.dump(event)

            # Remove the 'inscriptions' key from the event data
            if 'inscriptions' in event_data:
                del event_data['inscriptions']
            
            # Append the modified event data to the list
            modified_events.append(event_data)
        
        # Return the modified event data
        return modified_events, 200

class EventResource(Resource):
    '''
    Class that represents the Event Resource
    '''
    
    def get(self, event_code):
        # Find the event by the event code
        event = event_service.find_by_code(event_code)
        
        # Serialize the event data
        event_data = event_schema.dump(event)
        
        # Remove the 'inscriptions' key if present
        if 'inscriptions' in event_data:
            del event_data['inscriptions']
        
        # Return the event data
        return event_data, 200
