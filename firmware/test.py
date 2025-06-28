from tenta import Tentacle

gripper = Tentacle()

for i in range(150):
    gripper.servos["base"].angle = i