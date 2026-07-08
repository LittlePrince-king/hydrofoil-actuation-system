from abc import ABC, abstractmethod


class Protocol(ABC):
    """
    Converts Python values to bytes and bytes back to Python values.
    """

    @abstractmethod
    def encode(self, value) -> bytes:
        pass

    @abstractmethod
    def decode(self, data: bytes):
        pass