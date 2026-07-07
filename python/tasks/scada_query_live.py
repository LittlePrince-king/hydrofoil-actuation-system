import time
import math

# ---------------- CONFIG ----------------
MIN_ANGLE = 0
MAX_ANGLE = 180
PERIOD = 4.0

INTERNAL_HZ = 20
DT = 1 / INTERNAL_HZ

data = []

print("SCADA Running (Live Query Mode)")
print("Type a time value like 1.5 and press Enter")
print("Type 'exit' to stop\n")

start = time.time()

# ---------------- DATA GENERATION ----------------
for i in range(200):

    t = time.time() - start

    angle = (MIN_ANGLE + MAX_ANGLE)/2 + \
            (MAX_ANGLE - MIN_ANGLE)/2 * math.sin(2 * math.pi * t / PERIOD)

    data.append((t, angle))

    time.sleep(DT)

# ---------------- QUERY LOOP (REAL SCADA BEHAVIOR) ----------------
while True:

    user_input = input("\nQuery time (seconds): ")

    if user_input.lower() == "exit":
        break

    try:
        q = float(user_input)

        closest = min(data, key=lambda x: abs(x[0] - q))

        print(f"t={q}s → nearest t={closest[0]:.2f}s | angle={closest[1]:.2f}")

    except:
        print("Invalid input")