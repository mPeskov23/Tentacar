from tenta import Tentacle
from time import sleep

vision = 42

gripper = Tentacle(vision)

for i in range(150):
    gripper.servos["base"].angle = i
    sleep(0.2)
    