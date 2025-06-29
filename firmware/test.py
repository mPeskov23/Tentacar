from car import Car
from time import sleep

car = Car()

car.move_forward()
sleep(1)
car.speed = car.speed * 1.1
car.move_forward()
sleep(1)
car.speed = car.speed * 1.1
car.move_forward()
sleep(1)
car.speed = car.speed * 1.1
car.move_forward()
sleep(1)

car.stop()
car.cleanup()
