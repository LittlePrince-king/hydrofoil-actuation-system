import time
import threading

from .signals import SineWave
from .historian import Historian
from .hardware import ArduinoDriver
from .sim_driver import SimDriver


class SCADA:

    def __init__(self, port="COM3", baud=115200, mode="auto"):

        self.port = port
        self.baud = baud
        self.mode = mode

        # hardware
        try:
            self.hardware = ArduinoDriver(port=port, baud=baud)
            self.hardware.connect()
        except:
            self.hardware = SimDriver()
            self.hardware.connect()

        self.signal = SineWave(amplitude=90, frequency=0.2)
        self.historian = Historian()

        self.running = False
        self.dt = 1 / 20

        # IMPORTANT: prevent duplicate threads in Flask reload
        self.thread_started = False

        self.thread = threading.Thread(target=self._loop, daemon=True)

    # SAFE START (prevents duplicate loop)
    def start(self):
        self.running = True

        if not self.thread_started:
            self.thread.start()
            self.thread_started = True

    def stop(self):
        self.running = False

    # CONTROL LOOP (NO PRINTS ALLOWED)
    def _loop(self):

        while True:

            if self.running:

                t = time.time()

                ideal = self.signal.value(t)
                commanded = ideal

                try:
                    self.hardware.write(commanded)
                    measured = self.hardware.read()
                    if measured is None:
                        measured = commanded
                except:
                    measured = commanded

                self.historian.log(
                    timestamp=t,
                    ideal=ideal,
                    commanded=commanded,
                    measured=measured
                )

            time.sleep(self.dt)

    def set_signal(self, freq=None, amp=None):
        if freq is not None:
            self.signal.frequency = freq
        if amp is not None:
            self.signal.amplitude = amp

    def set_sampling(self, rate):
        self.dt = 1.0 / rate

    def data(self, n=1000):
        return self.historian.latest(n)

    def query(self, start, end):
        return self.historian.query(start, end)

    def run_procedure(self, amplitude=90, frequency=0.2, duration=10, sampling=20):

        self.set_signal(freq=frequency, amp=amplitude)
        self.set_sampling(sampling)

        self.start()

        start_time = time.time()

        while time.time() - start_time < duration:
            time.sleep(0.05)

        self.stop()

        return self.query(start_time, time.time())

    def close(self):
        self.running = False
        try:
            self.hardware.close()
        except:
            pass

