import time

def avoid_obstacle(car):
    car.turn_right(rotation=1)
    car.move_forward()
    car.turn_left(rotation=1)
    time.sleep(0.1)

def bug2(car, vision, object_threshold=25, wall_threshold=10):
    detections = vision.get_detections()
    distance = vision.get_nearest_object_distance()

    if not detections.detections:
        if 0 < distance < wall_threshold:
            avoid_obstacle(car)
        else:
            car.turn_left()
        return False

    bbox = detections.detections[0].bounding_box
    bbox_center_x = bbox.origin_x + bbox.width // 2
    frame_center_x = 1280 // 2
    offset = bbox_center_x - frame_center_x

    if abs(offset) > 50:
        rotation = int(abs(offset) / 100) + 1
        if offset > 0:
            car.turn_right(rotation)
        else:
            car.turn_left(rotation)

    while True:
        distance = vision.get_nearest_object_distance()

        if 0 < distance < wall_threshold:
            avoid_obstacle(car)
            return False

        if 0 < distance < object_threshold:
            car.stop()
            return True

        car.move_forward()
        time.sleep(0.1)
