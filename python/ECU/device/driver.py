from ..protocol.raw_byte import RawByteProtocol


class ArduinoDriver:
    """
    Device abstraction layer.

    Handles:
    - commands
    - protocol encoding/decoding

    Does NOT handle:
    - serial
    - TCP
    - COM ports
    """

    def __init__(self, transport, protocol=None):

        self.transport = transport
        self.protocol = protocol or RawByteProtocol()

    def connect(self):

        self.transport.connect()
        print("[ARDUINO] Connected")

    def write(self, value):

        data = self.protocol.encode(value)

        self.transport.write(data)

    def read(self):

        raw = self.transport.read()

        if raw is None:
            return None

        return self.protocol.decode(raw)

    def close(self):

        self.transport.close()