import cv2
from picamera2 import Picamera2

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

import utils_vision as utils

class VisionModule:
    def __init__(self, num_threads = 2):
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
        distance = 0 # Integrar un US (o 2)
        return distance