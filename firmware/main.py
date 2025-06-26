from vision import VisionModule
from car import Car
from tenta import Tentacle
from time import time
from bug2_module import bug2

def main():
    car = Car()
    vision = VisionModule(num_threads=2)
    tentacle = Tentacle(vision)

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
                success = bug2(car, vision)
                if not success:
                    continue
            else:
                car.stop()
                success = tentacle.grab_object()
                if success:
                    tentacle.place_in_basket()

            time.sleep(0.1)

    except KeyboardInterrupt:
        car.stop()
        car.cleanup()

if __name__ == "main":
    main()

