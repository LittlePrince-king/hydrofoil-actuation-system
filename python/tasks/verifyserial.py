from ECU.transport.serial import SerialTransport
import serial.tools.list_ports

"""
t11_verifyserial.py

Purpose:
Verify the serial transport layer can discover and communicate
with the Arduino.
"""

# Find first available serial port
ports = list(serial.tools.list_ports.comports())

if not ports:
    raise RuntimeError("No serial devices found.")

port = ports[0].device

print(f"[INFO] Using {port}")

transport = SerialTransport(port=port)

transport.connect()

print("[PASS] Connected")

transport.close()

print("[PASS] Serial transport verified")