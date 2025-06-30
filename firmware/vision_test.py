import cv2
import time
from vision import VisionModule
from car import Car
import utils_vision as utils

vision = VisionModule()
car = Car()

for i in range(3):

    frame = vision.picam2.capture_array()
    frame = cv2.flip(frame, -1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    tensor = vision.vision.TensorImage.create_from_array(frame_rgb)
    detections = vision.detector.detect(tensor)

    annotated = utils.visualize(frame, detections)

    cv2.imwrite("1.png", annotated)

    print("Press any button to continue")
    cv2.waitKey(0)
    car.turn_left(3)

cv2.destroyAllWindows()
