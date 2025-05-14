from vision import VisionModule
import tenta
import car

def main():
    c = car.Car()
    tentacle = tenta.Tentacle()
    vision = VisionModule(num_threads=2)

    while True():
        detections = vision.get_detections()
        distance = vision.get_nearest_object_distance()
        if distance == None:
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
