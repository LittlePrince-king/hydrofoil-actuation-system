from ECU.transport.serial import SerialTransport
from ECU.device.driver import ArduinoDriver
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())

if not ports:
    raise RuntimeError("No Arduino found")

transport = SerialTransport(port=ports[0].device)

driver = ArduinoDriver(
    transport=transport
)

driver.connect()

print("[PASS] Connected")

driver.write(1)

print("[PASS] LED ON command sent")

time.sleep(2)

driver.write(0)

print("[PASS] LED OFF command sent")

driver.close()