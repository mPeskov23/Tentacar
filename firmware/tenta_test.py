from tenta import Tentacle
from time import sleep

tenta = Tentacle(42)

tenta.servos["base"].angle = 0
sleep(1)
tenta.servos["arm"].angle = 0
sleep(1)
tenta.servos["grip"].angle = 0
sleep(1)

tenta.servos["base"].angle = 180
sleep(1)
tenta.servos["arm"].angle = 180
sleep(1)
tenta.servos["grip"].angle = 180
sleep(1)

tenta.servos["base"].angle = 0
sleep(1)
tenta.servos["arm"].angle = 0
sleep(1)
tenta.servos["grip"].angle = 0
sleep(1)
