from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def write(self, data: bytes):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def close(self):
        pass