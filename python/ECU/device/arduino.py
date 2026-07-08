```python
from hardware_interface import HardwareInterface
from protocol.raw_byte import RawByteProtocol


class Arduino(HardwareInterface):
    """
    Hardware abstraction for a microcontroller.

    This class does NOT know anything about:
        - Serial
        - TCP
        - USB
        - SCADA
        - Signals

    It only knows how to:
        connect
        write
        read
        close

    The transport object performs communication.
    The protocol object converts values to bytes.
    """

    def __init__(self, transport, protocol=None):

        self.transport = transport
        self.protocol = protocol or RawByteProtocol()

    def connect(self):
        self.transport.connect()

    def write(self, value):

        packet = self.protocol.encode(value)
        self.transport.write(packet)

    def read(self):

        raw = self.transport.read()

        if raw is None:
            return None

        return self.protocol.decode(raw)

    def close(self):
        self.transport.close()
```