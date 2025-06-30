from tenta import Tentacle
from time import sleep

tenta = Tentacle(42)

tenta.servos["base"].angle = 0
sleep(1)
tenta.servos["base"].angle = 45
sleep(1)

tenta.servos["base"].angle = 90
sleep(1)

tenta.servos["base"].angle = 135
sleep(1)

tenta.servos["base"].angle = 180
sleep(1)