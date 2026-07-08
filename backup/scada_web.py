import serial
import time
import math

# =========================
# CONFIG
# =========================
PORT = "COM3"      # your confirmed port
BAUD = 115200

# =========================
# CONNECT ARDUINO
# =========================
print("Connecting to Arduino...")

arduino = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

print("Arduino connected on", PORT)

# =========================
# SINE WAVE CONTROL LOOP
# =========================
start_time = time.time()

def get_sine_angle(t):
    # sine wave mapped to 0–180 degrees
    return (math.sin(t) + 1) * 90

# =========================
# MAIN LOOP
# =========================
while True:

    t = time.time() - start_time

    angle = get_sine_angle(t)

    msg = f"{angle}\n"
    arduino.write(msg.encode())

    print("Angle sent:", round(angle, 2))

    time.sleep(0.02)  # 50 Hz smooth control