class ArduinoController:
    def __init__(self):
        print("ArduinoController initialized (simulation mode)")

    def start(self, min_angle, max_angle, time_between):
        print(f"Wave config → min:{min_angle}, max:{max_angle}, period:{time_between}")


# test run
arduino = ArduinoController()

arduino.start(20, 40, 1000)
arduino.start(10, 60, 500)
