from ECU.transport.serial import SerialTransport
from ECU.device.driver import ArduinoDriver
import serial.tools.list_ports
import time

"""
t22_lightbulb_dimmer.py

Verify analog/PWM control through:

ArduinoDriver
      ↓
SerialTransport
      ↓
Arduino PWM LED
"""

ports = list(serial.tools.list_ports.comports())

if not ports:
    raise RuntimeError("No Arduino found")

transport = SerialTransport(port=ports[0].device)

driver = ArduinoDriver(
    transport=transport
)

driver.connect()

print("[PASS] Connected")

levels = [0, 64, 128, 192, 255]

for level in levels:
    print(f"[TEST] Brightness {level}")

    driver.write(level)

    time.sleep(1)

driver.close()

print("[PASS] Dimmer test complete")