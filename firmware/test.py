from tenta import Tentacle

vision = 42

gripper = Tentacle(vision)

for i in range(150):
    gripper.servos["base"].angle = i