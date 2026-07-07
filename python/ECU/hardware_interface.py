from abc import ABC, abstractmethod


class HardwareInterface(ABC):

    @abstractmethod
    def connect(self):
        pass


    @abstractmethod
    def write(self, value):
        pass


    @abstractmethod
    def read(self):
        return None


    @abstractmethod
    def close(self):
        pass

