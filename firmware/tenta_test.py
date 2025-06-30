from tenta import Tentacle
from time import sleep

tenta = Tentacle(42)

tenta.servos["base"].angle = 90
sleep(1)
tenta.servos["base"].angle = 140
sleep(1)

tenta.servos["base"].angle = 10
sleep(1)