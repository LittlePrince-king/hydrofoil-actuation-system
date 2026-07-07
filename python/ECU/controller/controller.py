import time

class Controller:
    def __init__(self, signal, hardware, historian):
        self.signal = signal
        self.hardware = hardware
        self.historian = historian
        self.start_time = None

    def connect(self):
        self.hardware.connect()

    def run_sine(self, rate=50):
        self.start_time = time.time()
        dt = 1 / rate

        print("Running SCADA system... Ctrl+C to stop")

        while True:
            t = time.time() - self.start_time
            angle = self.signal.value(t)

            self.hardware.write(angle)
            self.historian.log(t, angle)

            time.sleep(dt)