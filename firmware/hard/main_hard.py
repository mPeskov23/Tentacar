from car_hard import Car
from tenta_hard import Tentacle
import time

gripper = Tentacle()
car = Car()



for i in range(6):
    gripper.set_angle('arm', 90)
    car.move_forward()
    time.sleep(0.5)