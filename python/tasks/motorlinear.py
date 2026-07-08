from ECU.device.sim_driver import SimDriver
from ECU.device.driver import ArduinoDriver
import time


def motor_linear(start=0, end=100, steps=5):

    driver = ArduinoDriver(
        transport=SimDriver()
    )

    driver.connect()

    print("[MOTOR] Linear movement")

    positions = [
        start + i * (end-start)/(steps-1)
        for i in range(steps)
    ]

    for position in positions:

        driver.write(position)

        print(f"[COMMAND] {position}")

        time.sleep(0.5)

    driver.close()

    print("[PASS] Motor linear complete")


if __name__ == "__main__":
    motor_linear()