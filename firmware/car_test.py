from car import Car
from time import sleep

car = Car()

car.move_forward()
sleep(1)
car.turn_left()
car.move_forward()

car.turn_right(10)
car.move_forward()

car.stop()
car.cleanup()
