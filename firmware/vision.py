import cv2
from picamera2 import Picamera2

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

import utils_vision as utils
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG_PIN = 10
ECHO_PIN = 9

class VisionModule:
    def __init__(self, num_threads = 2):
        self.TRIG_PIN = TRIG_PIN
        self.ECHO_PIN = ECHO_PIN

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.TRIG_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)
        GPIO.output(self.TRIG_PIN, GPIO.LOW)
        time.sleep(0.1)
        
        self.model = 'efficientdet_lite0.tflite'
        self.num_threads = num_threads
        disp_width = 1280
        disp_height = 720

        self.picam2 = Picamera2()
        self.picam2.preview_configuration.main.size = (disp_width, disp_height)
        self.picam2.preview_configuration.main.format = 'RGB888'
        self.picam2.preview_configuration.align()
        self.picam2.configure("preview")

        self.picam2.start()

        base_options = core.BaseOptions(file_name = self.model, use_coral = False, num_threads = num_threads)
        detection_options = processor.DetectionOptions(max_results = 5, score_threshold = .5)
        options = vision.ObjectDetectorOptions(base_options = base_options, detection_options = detection_options)
        self.detector = vision.ObjectDetector.create_from_options(options)

    def get_detections(self):
        im = self.picam2.capture_array()
        im = cv2.flip(im, -1)
        im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im_tensor = vision.TensorImage.create_from_array(im_rgb)
        detections = self.detector.detect(im_tensor)
        #utils.visualize(im, detections)
        return detections
            
    def get_nearest_object_distance(self):
        GPIO.output(self.TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG_PIN, False)

        start_time = time.time()
        timeout = start_time + 0.04

        while GPIO.input(self.ECHO_PIN) == 0 and time.time() < timeout:
            start_pulse = time.time()
        
        while GPIO.input(self.ECHO_PIN) == 1 and time.time() < timeout:
            end_pulse = time.time()
        
        try:
            pulse_duration = end_pulse - start_pulse
            distance = pulse_duration * 17150
            distance = round(distance, 2)
        except:
            distance = -1
        
        return distance