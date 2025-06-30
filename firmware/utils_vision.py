import cv2
import numpy as np

_MARGIN = 10
_ROW_SIZE = 10
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_TEXT_COLOR = (0, 0, 255)

def visualize(image: np.ndarray, detections: list[dict]) -> np.ndarray:
    """
    Draw bounding boxes and class labels on the image.

    Args:
        image: The input RGB image (numpy array).
        detections: A list of dicts with keys: 'xmin', 'ymin', 'xmax', 'ymax', 'class', 'score'

    Returns:
        Annotated image.
    """
    for det in detections:
        start_point = (det['xmin'], det['ymin'])
        end_point = (det['xmax'], det['ymax'])
        cv2.rectangle(image, start_point, end_point, _TEXT_COLOR, 2)

        label = f"{det['class']} ({det['score']:.2f})"
        text_location = (_MARGIN + det['xmin'], _MARGIN + _ROW_SIZE + det['ymin'])
        cv2.putText(image, label, text_location, cv2.FONT_HERSHEY_PLAIN,
                    _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)

    return image
