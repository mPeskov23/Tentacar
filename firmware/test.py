from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

kit.servo[2].set_pulse_width_range(500, 2500)

kit.servo[2].angle = 100
time.sleep(2)
kit.servo[2].angle = 45
time.sleep(2)
