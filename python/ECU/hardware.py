import serial
from .hardware_interface import HardwareInterface


class ArduinoDriver(HardwareInterface):

    def __init__(self, port="COM3", baud=115200):

        self.port = port
        self.baud = baud
        self.ser = None
        self.simulation = False


    def connect(self):

        try:

            self.ser = serial.Serial(
                self.port,
                self.baud,
                timeout=1
            )

            print("[ARDUINO] Connected")

            self.simulation = False

        except Exception as e:

            print("[ARDUINO SIM MODE]", e)

            self.simulation = True


    def write(self, value):

        if self.simulation:

            return

        try:

            self.ser.write(bytes([int(value)]))

        except Exception as e:

            print("[WRITE ERROR]", e)


    def read(self):

        if self.simulation:

            return None

        try:

            return self.ser.readline()

        except:

            return None


    def close(self):

        if self.ser:

            self.ser.close()

