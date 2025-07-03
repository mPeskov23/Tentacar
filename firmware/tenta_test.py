from tenta import Tentacle
from time import sleep

tenta = Tentacle(42)

try:
    while True:
        print("0 degrees")
        for angle in range(180, -1, -1):
            try:
                tenta.servos["base"].angle = angle
                tenta.servos["shoulder"].angle = angle
                tenta.servos["arm"].angle = angle
                tenta.servos["grip"].angle = angle
                sleep(0.2)
            except KeyboardInterrupt:
                break

        input("Press Enter to continue")

        print("Smoothly moving to 45 degrees")
        tenta.smooth_move("base", 0, 45)
        tenta.smooth_move("shoulder", 0, 45)
        tenta.smooth_move("arm", 0, 45)
        tenta.smooth_move("grip", 0, 45)

        input("Press Enter to continue")

        print("Smoothly moving to 90 degrees")
        tenta.smooth_move("base", 45, 90)
        tenta.smooth_move("shoulder", 45, 90)
        tenta.smooth_move("arm", 45, 90)
        tenta.smooth_move("grip", 45, 90)

        input("Press Enter to continue")

        print("Smooth moving to 135 degrees")
        tenta.smooth_move("base", 90, 135)
        tenta.smooth_move("shoulder", 90, 135)
        tenta.smooth_move("arm", 90, 135)
        tenta.smooth_move("grip", 90, 135)

        break

except KeyboardInterrupt:
    print("Keyboard Interruption")

