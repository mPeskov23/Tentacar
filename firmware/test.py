from car import Car
from tenta import Tentacle
from time import sleep

car = Car(42)
tenta = Tentacle()

car.move_forward(2)
sleep(0.2)

car.turn_right(10)
sleep(0.2)
car.move_forward(2)
sleep(0.2)

car.turn_left(10)
sleep(0.2)

car.turn_right(10)
sleep(0.2)
car.move_forward(2)
sleep(0.2)

car.turn_left(10)
sleep(0.2)
car.move_forward(4)
sleep(0.2)
car.turn_left(5)
sleep(0.2)

car.move_forward(2)
sleep(2)
tenta.grab_test()
