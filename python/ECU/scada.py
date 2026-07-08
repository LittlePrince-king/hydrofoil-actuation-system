import time
import math

from .device.driver import ArduinoDriver
from .device.sim_driver import SimDriver
from .transport.serial import SerialTransport


class SCADA:
    """
    Procedure/control layer.

    User calls:
        SCADA.startservo()

    Internal:
        SCADA
          -> Driver
          -> Protocol
          -> Transport
          -> Arduino
    """

    def __init__(self, hardware=None):

        if hardware:
            self.hardware = hardware

        else:
            try:
                transport = SerialTransport.auto_detect()
                self.hardware = ArduinoDriver(transport)

            except Exception:
                print("[AUTO DETECT FAILED]", e)
                self.hardware = SimDriver()

        self.hardware.connect()


    def startservo(
        self,
        amplitude=45,
        duration=10,
        min_angle=45,
        max_angle=135,
        frequency=0.2
    ):

        center = (min_angle + max_angle) / 2

        start_time = time.time()

        while time.time() - start_time < duration:

            t = time.time() - start_time

            angle = (
                center
                + amplitude * math.sin(
                    2 * math.pi * frequency * t
                )
            )

            self.hardware.write(angle)

            print(f"[SERVO] {angle:.1f}")

            time.sleep(0.05)


    def close(self):
        self.hardware.close()