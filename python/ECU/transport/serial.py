import serial
import serial.tools.list_ports

from .transport import Transport


class SerialTransport(Transport):

    def __init__(self, port, baud=115200):
        self.port = port
        self.baud = baud
        self.conn = None


    @classmethod
    def auto_detect(cls, baud=115200):
        """
        Automatically find an available serial device.

        Returns:
            SerialTransport object
        """

        ports = serial.tools.list_ports.comports()

        if not ports:
            raise RuntimeError("No serial devices found")

        for port in ports:
            try:
                return cls(
                    port.device,
                    baud
                )

            except Exception:
                continue

        raise RuntimeError("No usable serial device found")


    def connect(self):
        self.conn = serial.Serial(
            self.port,
            self.baud,
            timeout=1
        )


    def write(self, data: bytes):
        if self.conn:
            self.conn.write(data)


    def read(self):
        if self.conn:
            return self.conn.readline()

        return None


    def close(self):
        if self.conn:
            self.conn.close()