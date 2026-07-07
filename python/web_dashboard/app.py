from flask import Flask, jsonify, render_template, request
import time
import threading

from hydrofoil_scada import SCADA

app = Flask(__name__)

# =========================
# SCADA SYSTEM
# =========================

system = SCADA(port="COM3")

# IMPORTANT: DO NOT let Flask debug duplicate threads
system.start()

# =========================
# STATE
# =========================

# =========================
# ROUTES (HMI LAYER ONLY)
# =========================

@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/start")
def start():
    system.start()
    return jsonify({"status": "running"})


@app.route("/stop")
def stop():
    system.stop()
    return jsonify({"status": "stopped"})


@app.route("/set")
def set_params():

    freq = float(request.args.get("freq", 0.2))
    amp = float(request.args.get("amp", 90))

    system.set_signal(freq=freq, amp=amp)

    return jsonify({"frequency": freq, "amplitude": amp})


@app.route("/data")
def data():
    return jsonify(system.data(500))


@app.route("/query")
def query():

    start_t = float(request.args.get("start", 0))
    end_t = float(request.args.get("end", time.time()))

    return jsonify(system.query(start_t, end_t))


@app.route("/run")
def run():

    amp = float(request.args.get("amp", 90))
    freq = float(request.args.get("freq", 0.2))
    dur = float(request.args.get("dur", 5))

    result = system.run_procedure(
        amplitude=amp,
        frequency=freq,
        duration=dur
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

