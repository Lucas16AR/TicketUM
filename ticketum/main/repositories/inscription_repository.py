from .repository import Create, Read, Update, Delete
from .. import db
from main.models import InscriptionModel, EventModel, GuestModel


class InscriptionRepository(Create, Read, Update, Delete):
    '''
    Class to manage the CRUD operations of the InscriptionModel
    param:
        - Create: Abstract class to create a model
        - Read: Abstract class to read a model
        - Update: Abstract class to update a model
        - Delete: Abstract class to delete a model
    '''

    def __init__(self):
        self.model = InscriptionModel
        self.event_model = EventModel
        self.guest_model = GuestModel

    def create(self, model: object):
        db.session.add(model)
        db.session.commit()
        return model
    
    def find_all(self):
        return self.model.query.all()
    
    def find_by_id(self, id: int):
        return self.model.query.get(id)
    
    def find_by_event_guest_code(self, event_code: str, guest_code: str):
        return self.model.query.join(self.event_model).join(self.guest_model).filter(
            self.event_model.event_code == event_code,
            self.guest_model.guest_code == guest_code
        ).first()
    
    def update(self, inscription):
        db.session.merge(inscription)
        db.session.flush()
        db.session.commit()
        return inscription
    
    def delete(self, id: int):
        model = self.model.query.get(id)
        db.session.delete(model)
        db.session.commit()
        return model