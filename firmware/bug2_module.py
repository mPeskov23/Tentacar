def bug2(car, vision, distance_threshold=15):
    detections = vision.get_detections()
    if not detections.detections:
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

        if 0 < distance < distance_threshold:
            car.stop()
            return True

        detections = vision.get_detections()
        if not detections.detections:
            return False

        car.move_forward()
