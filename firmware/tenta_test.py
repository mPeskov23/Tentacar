from tenta import Tentacle
from time import sleep

tenta = Tentacle(42)

tenta.servos["base"].angle = 0
tenta.servos["arm"].angle = 0
tenta.servos["grip"].angle = 0

sleep(2)

tenta.servos["base"].angle = 45
tenta.servos["arm"].angle = 45
tenta.servos["grip"].angle = 45

sleep(2)

tenta.servos["base"].angle = 90
tenta.servos["arm"].angle = 90
tenta.servos["grip"].angle = 90

sleep(2)

tenta.servos["base"].angle = 135
tenta.servos["arm"].angle = 135
tenta.servos["grip"].angle = 135

sleep(2)

tenta.servos["base"].angle = 180
tenta.servos["arm"].angle = 180
tenta.servos["grip"].angle = 180

sleep(2)
