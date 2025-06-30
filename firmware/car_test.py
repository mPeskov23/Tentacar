from car import Car
from time import sleep

car = Car()

car.move_forward(1)
sleep(1)
car.turn_left()
car.move_forward(2)

car.turn_right(10)
car.move_forward(3)

car.stop()
car.cleanup()
