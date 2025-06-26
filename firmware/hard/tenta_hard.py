import math
import time
import numpy as np
from pca9685_driver import Device

class Tentacle:
    def __init__(self):
        self.pca = Device(0x40)
        self.pca.set_pwm_frequency(50)

        self.servos = {
            'base': 0,
            'arm': 1,
            'grip': 2
        }

        self.set_angle('arm', 90)
        time.sleep(0.5)

    def angle_to_pwm(self, angle):
        pulse_min = 205
        pulse_max = 410
        pwm_val = int(pulse_min + (pulse_max - pulse_min) * (angle / 180.0))
        return int(np.clip(pwm_val, 205, 410))

    def set_angle(self, name, angle):
        channel = self.servos.get(name)
        if channel is not None:
            pwm = self.angle_to_pwm(angle)
            self.pca.set_pwm(channel, pwm) 


    def reset_position(self):
        self.set_angle('base', 0)
        self.set_angle('arm', 90)
        self.set_angle('grip', 90)
        time.sleep(0.5)

    def get_target_coordinates(self):
        detections = self.vision.get_detections()
        if not detections or len(detections.detections) == 0:
            return None

        detection = detections.detections[0]
        bbox = detection.bounding_box
        cx = (bbox.origin_x + bbox.width / 2) / 1280
        cy = (bbox.origin_y + bbox.height / 2) / 720 
        return cx, cy
    
    def get_servo_angles_from_coords(self, cx, cy):
        base_angle = int((1.0 - cx) * 90)
        arm_angle = int((1.0 - cy) * 90)
        return base_angle, arm_angle

    def get_ik_angles(self, x_cm, y_cm):
        L1, L2 = 20, 31
        dist = math.hypot(x_cm, y_cm)
        if dist > L1 + L2:
            return None

        cos_angle = (x_cm**2 + y_cm**2 - L1**2 - L2**2) / (2 * L1 * L2)
        angle2 = math.acos(cos_angle)
        k1 = L1 + L2 * math.cos(angle2)
        k2 = L2 * math.sin(angle2)
        angle1 = math.atan2(y_cm, x_cm) - math.atan2(k2, k1)

        return math.degrees(angle1), math.degrees(angle2)

    def grab_object(self):
        coords = self.get_target_coordinates()
        if not coords:
            return False

        cx, cy = coords
        base_angle, arm_angle = self.get_servo_angles_from_coords(cx, cy)

        self.set_angle('grip', 90)
        time.sleep(0.5)
        self.set_angle('base', base_angle)
        time.sleep(0.5)
        self.set_angle('arm', arm_angle)
        time.sleep(0.5)
        self.set_angle('grip', 0)
        time.sleep(0.5)
        self.set_angle('arm', 0)
        time.sleep(0.5)
        self.set_angle('base', 180)
        time.sleep(0.5)
        self.set_angle('grip', 90)
        time.sleep(0.5)
        self.reset_position()

        return True
