from abc import ABC, abstractmethod

class Service(ABC):
    '''
    Abstract class with the abstract methods to create a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod
    def create(self, model: object):
        '''
        Method to create a model
        param:
            - object: Object to create
        '''
        pass

    @abstractmethod
    def find_all(self):
        '''
        Method to find all models
        '''
        pass

    @abstractmethod
    def find_by_id(self, id: int):
        '''
        Method to find a model by its id
        '''
        pass

    @abstractmethod
    def update(self, model: object):
        '''
        Method to update a model
        '''
        pass

    @abstractmethod
    def delete(self, object):
        '''
        Method to delete a model
        '''
        pass