from car import Car
from tenta import Tentacle
from time import sleep

car = Car()

car.move_forward(1)
sleep(1)
car.turn_left(7)
car.move_forward(2)


car.turn_right(10)
car.move_forward(3)

car.stop()

t = Tentacle(42)

t.servos["arm"].angle = 100
sleep(0.5)

t.smooth_move("shoulder", 0, 165, 5)
sleep(0.5)

t.reset()
sleep(0.5)

t.servos["base"].angle = 90
sleep(2)

t.reset()