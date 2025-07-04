from tenta import Tentacle
from time import sleep

t = Tentacle(42)

t.servos["base"].angle = 90
sleep(2)

t.servos["base"].angle = 0
sleep(2)

t.servos["arm"].angle = 90
sleep(2)

t.servos["arm"].angle = 0
sleep(2)

t.servos["shoulder"].angle = 90
sleep(2)

t.servos["shoulder"].angle = 0