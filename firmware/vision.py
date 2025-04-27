import cv2
from picamera2 import Picamera2

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

import utils_vision

model = 'efficientdet_lite0.tflite'
num_threads = 4
disp_width = 1280
disp_height = 720

picam2 = Picamera2()
picam2.preview_configuration.main.size = (disp_width, disp_height)
picam2.preview_configuration.main.format = 'RGB888'
picam2.preview_configuration.align()
picam2.configure("preview")

picam2.start()

base_options = core.BaseOptions(file_name = model, use_coral = False, num_threads = num_threads)
detection_options = processor.DetectionOptions(max_results = 5, score_threshold = .5)
options = vision.ObjectDetectorOptions(base_options = base_options, detection_options = detection_options)
detector = vision.ObjectDetector.create_from_options(options)

while True:
    im = picam2.capture_array()
    im = cv2.flip(im, -1)
    im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im_tensor = vision.TensorImage.create_from_array(im_rgb)
    detections = detector.detect(im_tensor)