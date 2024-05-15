from main.repositories import GuestRepository
from .service import Service
from main.models import GuestModel

class GuestService(Service):
    '''
    Class that represents the service of the Entity Guest
    param:
        - Service: Class that inherits from the Service interface
    '''

    def __init__(self):
        self.__repository = GuestRepository()

    def create(self, name: str, email: str, phone: str, dni: int):
        guest_model = GuestModel(
            name=name,
            email=email,
            phone=phone,
            dni=dni
        )
        return self.__repository.create(guest_model)

    def find_all(self):
        return self.__repository.find_all()
    
    def find_by_id(self, id: int):
        return self.__repository.find_by_id(id)
    
    def update(self, id: int, name: str, email: str, phone: str, dni: int):

        guest_model = GuestModel(
            id=id,
            name=name,
            email=email,
            phone=phone,
            dni=dni
        )
        return self.__repository.update(guest_model)
    
    def delete(self, id: int):
        return self.__repository.delete(id)