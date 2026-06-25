class FakeArduino:
    def write(self, data):
        print("Arduino received:", data.decode().strip())


class ArduinoController:
    def __init__(self):
        self.serial = FakeArduino()

    def start(self, angle):
        self.serial.write(f"{angle}\n".encode())


# test
arduino = ArduinoController()

arduino.start(90)
arduino.start(45)
arduino.start(120)
