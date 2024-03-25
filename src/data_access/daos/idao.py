from abc import ABC, abstractmethod

class IDao(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create(self, record):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self, record):
        pass

    @abstractmethod
    def delete(self, record):
        pass