import serial
import time
import math
from flask import Flask, request, jsonify, render_template_string

# =========================
# CONFIG
# =========================
PORT = "COM3"
BAUD = 115200

arduino = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

# =========================
# DATA STORAGE (HISTORIAN)
# =========================
history = []

start_time = time.time()

# =========================
# FLASK APP
# =========================
app = Flask(__name__)

# =========================
# SINE FUNCTION (IDEAL MODEL)
# =========================
def sine_wave(t):
    return (math.sin(t) + 1) * 90  # 0–180

# =========================
# CONTROL LOOP
# =========================
def control_loop():
    while True:
        t = time.time() - start_time

        angle = sine_wave(t)

        # send to Arduino
        msg = f"{angle}\n"
        arduino.write(msg.encode())

        # store history (ideal vs actual placeholder)
        history.append({
            "t": t,
            "ideal": angle
        })

        if len(history) > 2000:
            history.pop(0)

        time.sleep(0.02)  # 50 Hz

# =========================
# DASHBOARD UI
# =========================
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SCADA Sine Dashboard</title>
</head>
<body>
<h2>SCADA Sine Wave System</h2>

<button onclick="loadData()">Load Graph</button>

<canvas id="chart" width="800" height="400"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>

async function loadData() {
    let res = await fetch('/data');
    let data = await res.json();

    let t = data.map(d => d.t);
    let ideal = data.map(d => d.ideal);

    new Chart(document.getElementById('chart'), {
        type: 'line',
        data: {
            labels: t,
            datasets: [
                {
                    label: "Ideal Sine",
                    data: ideal,
                    borderColor: "blue",
                    fill: false
                }
            ]
        }
    });
}

</script>

</body>
</html>
"""

# =========================
# ROUTES
# =========================
@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/data")
def data():
    return jsonify(history)

# =========================
# START SYSTEM
# =========================
if __name__ == "__main__":
    import threading

    t = threading.Thread(target=control_loop, daemon=True)
    t.start()

    app.run(debug=True, use_reloader=False)