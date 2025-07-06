import cv2
from picamera2 import Picamera2
import numpy as np
import tflite_runtime.interpreter as tflite
import RPi.GPIO as GPIO
import time

TRIG_PIN = 10
ECHO_PIN = 9

class VisionModule:
    def __init__(self):
        self.model = "efficientdet_lite0.tflite"
        self.interpreter = tflite.Interpreter(model_path=self.model)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        input_shape = self.input_details[0]['shape']
        self.input_height = input_shape[1]
        self.input_width = input_shape[2]

        self.picam2 = Picamera2()
        self.picam2.preview_configuration.main.size = (1280, 720)
        self.picam2.preview_configuration.main.format = 'RGB888'
        self.picam2.preview_configuration.align()
        self.picam2.configure("preview")
        self.picam2.start()

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(TRIG_PIN, GPIO.OUT)
        GPIO.setup(ECHO_PIN, GPIO.IN)
        GPIO.output(TRIG_PIN, GPIO.LOW)
        time.sleep(0.1)

    def get_detections(self):
        frame = self.picam2.capture_array()
        frame = cv2.flip(frame, -1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(rgb, (self.input_width, self.input_height))
        input_tensor = np.expand_dims(resized, axis=0).astype(np.uint8)

        self.interpreter.set_tensor(self.input_details[0]['index'], input_tensor)
        self.interpreter.invoke()

        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])[0]  # [N,4]
        classes = self.interpreter.get_tensor(self.output_details[1]['index'])[0]  # [N]
        scores = self.interpreter.get_tensor(self.output_details[2]['index'])[0]  # [N]
        count = int(self.interpreter.get_tensor(self.output_details[3]['index'])[0])  # scalar

        detections = []
        for i in range(count):
            if scores[i] > 0.5:
                y_min, x_min, y_max, x_max = boxes[i]
                bbox = {
                    'xmin': int(x_min * 1280),
                    'ymin': int(y_min * 720),
                    'xmax': int(x_max * 1280),
                    'ymax': int(y_max * 720),
                    'class': int(classes[i]),
                    'score': float(scores[i])
                }
                detections.append(bbox)

        return detections

    def get_nearest_object_distance(self):
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)

        start_time = time.time()
        timeout = start_time + 0.04

        while GPIO.input(ECHO_PIN) == 0 and time.time() < timeout:
            start_pulse = time.time()
        
        while GPIO.input(ECHO_PIN) == 1 and time.time() < timeout:
            end_pulse = time.time()
        
        try:
            pulse_duration = end_pulse - start_pulse
            distance = pulse_duration * 17150
            distance = round(distance, 2)
        except:
            distance = -1
        
        return distance
