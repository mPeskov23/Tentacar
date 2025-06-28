from tenta import Tentacle
from vision import VisionModule

vision = VisionModule

gripper = Tentacle(vision)

for i in range(150):
    gripper.servos["base"].angle = i