from car_hard import Car
from tenta_hard import Tentacle
import time

gripper = Tentacle()

for i in range(6):
    gripper.set_angle('arm', 90)
    time.sleep(0.5)