from tenta import Tentacle

tenta = Tentacle(42)

try:
    while True:
        print("0 degrees")
        tenta.servos["base"].angle = 0
        tenta.servos["arm"].angle = 0
        tenta.servos["grip"].angle = 0

        input("Press Enter to continue")

        print("Smoothly moving to 45 degrees")
        tenta.smooth_move("base", 0, 45)
        tenta.smooth_move("arm", 0, 45)
        tenta.smooth_move("grip", 0, 45)

        input("Press Enter to continue")

        print("Smoothly moving to 90 degrees")
        tenta.smooth_move("base", 45, 90)
        tenta.smooth_move("arm", 45, 90)
        tenta.smooth_move("grip", 45, 90)

        input("Press Enter to continue")

        print("Smooth moving to 135 degrees")
        tenta.smooth_move("base", 90, 135)
        tenta.smooth_move("arm", 90, 135)
        tenta.smooth_move("grip", 90, 135)

        input("Press Enter to repeat")

except KeyboardInterrupt:
    print("Keyboard Interruption")

