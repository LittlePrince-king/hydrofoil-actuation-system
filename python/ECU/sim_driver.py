from .hardware_interface import HardwareInterface


class SimDriver(HardwareInterface):

    def __init__(self):
        self.last_value = 0

    def connect(self):
        print("[SIM] Connected")

    def write(self, value):
        # store command exactly
        self.last_value = int(value)

    def read(self):
        # PERFECT SCADA MODEL:
        # actual follows command exactly
        return self.last_value

    def close(self):
        pass

