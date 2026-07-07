from hydrofoil_scada import Controller, SineWave, ArduinoDriver, Historian

signal = SineWave()

hardware = ArduinoDriver(port="COM3")
hist = Historian()

controller = Controller(signal, hardware, hist)

controller.connect()
controller.run_sine()