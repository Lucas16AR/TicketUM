from abc import ABC, abstractmethod
from .. import db

class Create(ABC):
    '''
    Abstract class with the abstract methods to create a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod
    def create(self, object):
        '''
        Method to create a model
        param:
            - object: Object to create
        '''
        pass

class Read(ABC):
    '''
    Abstract class with the abstract methods to read a model
    param:
        - ABC: Abstract class from which it inherits
    '''

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

class Update(ABC):
    '''
    Abstract class with the abstract methods to update a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod
    def update(self, model: object):
        '''
        Method to update a model
        '''
        pass

class Delete(ABC):
    '''
    Abstract class with the abstract methods to delete a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod
    def delete(self, object):
        '''
        Method to delete a model
        '''
        pass 

    @abstractmethod
    def delete_by_id(self, id: int):
        '''
        Method to delete a model by its id
        '''
        pass