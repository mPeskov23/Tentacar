from vision import VisionModule
from car import Car
from tenta import Tentacle
from time import time

def main():
    car = Car()
    tentacle = Tentacle()
    vision = VisionModule(num_threads=2)

    OBJECT_DISTANCE_THRESHOLD = 25
    SCAN_TURN_DURATION = 0.5

    try:
        while True:
            detections = vision.get_detections()
            distance = vision.get_nearest_object_distance()

            if len(detections.detections) == 0:
                car.turn_left()
                time.sleep(SCAN_TURN_DURATION)
                car.stop()
                continue

            if distance > OBJECT_DISTANCE_THRESHOLD or distance == -1:
                car.move_forward()
            else:
                car.stop()
                success = tentacle.grab()
                if success:
                    tentacle.place_in_basket()

            time.sleep(0.1)

    except KeyboardInterrupt:
        car.stop()

if __name__ == "main":
    main()

