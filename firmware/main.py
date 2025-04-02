import vision
import tenta
import car

def main():
    c = car.Car()
    tentacle = tenta.Tentacle()

    while True():
        scene = vision.get_scene()
        coordinates = vision.get_object_coordinates(scene)
        if coordinates == None:
            car.turn_right()
            continue
        else:
            c.move_forward() # TODO: Movement logic
            tentacle.get_object()
            tentacle.move_object()
            break
    pass

if __name__ == "__main__":
    main()
