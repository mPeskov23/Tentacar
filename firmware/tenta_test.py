from tenta import Tentacle
from time import sleep

t = Tentacle(42)

t.servos["arm"].angle = 100
sleep(0.5)

t.smooth_move("shoulder", 0, 165, 5)
sleep(0.5)

t.reset()
sleep(0.5)

t.servos["base"].angle = 90
sleep(0.5)

t.reset()