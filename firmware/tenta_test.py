from tenta import Tentacle

tenta = Tentacle(42)

print("0 degrees")

tenta.servos["base"].angle = 0
tenta.servos["arm"].angle = 0
tenta.servos["grip"].angle = 0

input("Press Enter to continue")

print("smoothly moving to 45 degrees")

tenta.smooth_move("base", 0, 45)
tenta.smooth_move("arm", 0, 45)
tenta.smooth_move("grip", 0, 45)

input("Press enter to continue")

print("Quickly moving to 90 degrees")

tenta.servos["base"].angle = 90
tenta.servos["arm"].angle = 90
tenta.servos["grip"].angle = 90

input("Press enter to continue")

print("Smooth moving to 135 degrees")

tenta.smooth_move("base", 90, 135)
tenta.smooth_move("arm", 90, 135)
tenta.smooth_move("grip", 90, 135)

input("Press Enter to finish")

print("resetting position")
tenta.reset_position()
