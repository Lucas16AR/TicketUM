from main.repositories import InscriptionRepository
from .service import Service
from main.models import InscriptionModel

class InscriptionService(Service):
    '''
    Class that represents the service of the Entity Inscription
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = InscriptionRepository()

    def create(self, status: str, event_id: int, guest_id: int):

        inscription_model = InscriptionModel(
            status=status,
            event_id=event_id,
            guest_id=guest_id
        )
        return self.__repository.create(inscription_model)

    def find_all(self):
        return self.__repository.find_all()
    
    def find_by_id(self, id: int):
        return self.__repository.find_by_id(id)
    
    def find_by_event_guest_code(self, event_code: str, guest_code: str):
        return self.__repository.find_by_event_guest_code(event_code, guest_code)
    
    def update(self, id: int, status: str, event_id: int, guest_id: int):
        inscription_model = InscriptionModel(
            id=id,
            status=status,
            event_id=event_id,
            guest_id=guest_id
        )
        return self.__repository.update(inscription_model)
    
    def delete(self, id: int):
        return self.__repository.delete(id)