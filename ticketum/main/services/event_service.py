from main.repositories import EventRepository
from .service import Service
from main.models import EventModel
# Import datetime to handle the date of the event
from datetime import datetime

class EventService(Service):
    '''
    Class that represents the service of the Entity Event
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = EventRepository()

    def create(self, event_code: str, name: str, description: str, date, location: str, capacity: int):
        event_model = EventModel(
            event_code=event_code,
            name=name,
            description=description,
            date=date,
            location=location,
            capacity=capacity
        )
        return self.__repository.create(event_model)
    
    def find_all(self):
        return self.__repository.find_all()
    
    def find_by_id(self, id: int):
        return self.__repository.find_by_id(id)
    
    def update(self, id: int, event_code: str, name: str, description: str, date, location: str, capacity: int):

        event_model = EventModel(
            id=id,
            event_code=event_code,
            name=name,
            description=description,
            date=date,
            location=location,
            capacity=capacity
        )
        return self.__repository.update(event_model)
    
    def delete(self, id: int):
        return self.__repository.delete(id)