from .protocol import Protocol


class RawByteProtocol(Protocol):
    """
    Simple protocol:
    
    Python:
        90
    
    becomes:
        b'90\n'

    Used for basic Arduino serial communication.
    """

    def encode(self, value):
        return f"{int(value)}\n".encode("utf-8")

    def decode(self, data):
        if not data:
            return None

        try:
            return int(data.decode("utf-8").strip())

        except Exception:
            return None