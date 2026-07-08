from ECU.transport.serial import SerialTransport
from ECU.device.driver import ArduinoDriver

import serial.tools.list_ports

"""
t13_ping_mController.py

Verify:
ArduinoDriver
      ↓
Transport
      ↓
Arduino
"""

ports = list(serial.tools.list_ports.comports())

if not ports:
    raise RuntimeError("No Arduino detected.")

transport = SerialTransport(port=ports[0].device)

driver = ArduinoDriver(transport)

driver.connect()

print("[PASS] Driver connected")

driver.close()

print("[PASS] Microcontroller reachable")