import time
import board
import busio
from adafruit_servokit import ServoKit

class Tentacle:
    def __init__(self, max_angle=90, step=1, delay=0.1):
        i2c = busio.I2C(board.SCL, board.SDA)

        self.kit = ServoKit(channels=16, i2c=i2c)

        self.servos = {
            'a': self.kit.servo[0],
            'b': self.kit.servo[1],
            'c': self.kit.servo[2]
        }
        self.max_angle = max_angle
        self.step = step
        self.delay = delay
        self.target_angles = {key: 0 for key in self.servos}

        for servo in self.servos.values():
            servo.set_pulse_width_range(500, 2500)
            servo.angle = 0

    def grab(self):
        grabbing = True
        while grabbing:
            grabbing = False
            for key, servo in self.servos.items():
                current_angle = self.target_angles[key]
                next_angle = current_angle + self.step

                if next_angle > self.max_angle:
                    continue

                servo.angle = next_angle
                self.target_angles[key] = next_angle
                grabbing = True
                time.sleep(self.delay)

        return self.target_angles