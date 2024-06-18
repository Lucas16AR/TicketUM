from .repository import Create, Read, Update, Delete
from .. import db
from main.models import EventModel


class EventRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD operations of the EventModel
    param:
        - Create: Abstract class to create a model
        - Read: Abstract class to read a model
        - Update: Abstract class to update a model
        - Delete: Abstract class to delete a model
    '''

    def __init__(self):
        self.model = EventModel

    def create(self, model: object):
        db.session.add(model)
        db.session.commit()
        return model
    
    def find_all(self):
        return self.model.query.all()
    
    def find_by_id(self, id: int):
        return self.model.query.get(id)
    
    def find_by_code(self, code: str):
        return self.model.query.filter_by(event_code=code).first()
    
    def update(self, model: object):
        db.session.commit()
        return model
    
    def delete(self, id: int):
        model = self.model.query.get(id)
        db.session.delete(model)
        db.session.commit()
        return model