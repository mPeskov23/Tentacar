import math
import time
import board
import busio
from adafruit_servokit import ServoKit

class Tentacle:
    def __init__(self, vision_module):
        i2c = busio.I2C(board.SCL, board.SDA)

        self.kit = ServoKit(channels=16, i2c=i2c)

        self.vision = vision_module

        self.servos = {
            'grip': self.kit.servo[0],
            'arm': self.kit.servo[1],
            'shoulder': self.kit.servo[2],
            'base': self.kit.servo[3]
        }
        
        for servo in self.servos.values():
            servo.set_pulse_width_range(1000, 2000)

    def reset_position(self):
        self.servos['base'].angle = 0
        self.servos['shoulder'].angle = 90
        self.servos['arm'].angle = 90
        self.servos['grip'].angle = 90
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
    
    def get_servo_angles_from_coords(self, cx, cy): #Primera aproximación
        base_angle = int((1.0 - cx) * 90)
        arm_angle = int((1.0 - cy) * 90)
        return base_angle, arm_angle
    
    def get_ik_angles(self, x_cm, y_cm): #Para el futuro (necesitamos todas las medidas y unas cuantas pruebas)
        L1, L2 = 20, 31 #Aquí necesitaremos las medidas reales
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

        self.servos['grip'].angle = 90
        time.sleep(0.5)
        self.servos['base'].angle = base_angle
        time.sleep(0.5)
        self.servos['arm'].angle = arm_angle
        time.sleep(0.5)
        self.servos['grip'].angle = 0
        time.sleep(0.5)
        self.servos['arm'].angle = 0
        time.sleep(0.5)
        self.servos['base'].angle = 180
        time.sleep(0.5)
        self.servos['grip'].angle = 90
        time.sleep(0.5)
        self.reset_position()

        return True
    
    def grab_test(self):
        self.servos["base"].angle = 0
        time.sleep(0.1)
        self.servos["grip"].angle = 90
        time.sleep(0.1)
        self.servos["arm"].angle = 45
        time.sleep(0.1)
        self.servos["grip"].angle = 0
        time.sleep(0.1)
        self.servos["arm"].angle = 180
        time.sleep(0.1)
        self.servos["base"].angle = 180
        time.sleep(0.1)
        self.servos["grip"].angle = 180
        time.sleep(0.1)
        self.reset_position() 

    def smooth_move(self, servo_name, start, end):
        for angle in range(start, end):
            self.servos[servo_name].angle = angle
            print(servo_name, "has an angle ", angle)
            time.sleep(0.1)