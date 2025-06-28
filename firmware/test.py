from tenta import Tentacle
from time import sleep

vision = 42

gripper = Tentacle(vision)

gripper.servos["grip"].angle = 90
sleep(5)
gripper.servos["grip"].angle = 0
sleep(5)
gripper.servos["base"].angle = 90
sleep(5)
gripper.servos["base"].angle = 0
sleep(5)
gripper.servos["arm"].angle = 90
sleep(5)
gripper.servos["arm"].angle = 0
sleep(5)
    