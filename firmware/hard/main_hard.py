from car_hard import Car
from tenta_hard import Tentacle
car = Car()
car.move_forward()

gripper = Tentacle()

gripper.grab_object()


car.cleanup()