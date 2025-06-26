import cv2
OBJECT_THRESHOLD = 120 # pixel

def objectes_petits(det):
    
    objectes = []
    for detection in det:
        bbox = detection.bounding_box
        bbox_w = bbox.xmax - bbox.xmin
        if (bbox_w <= OBJECT_THRESHOLD):
            objectes.append(detection)
    return objectes

# OPCION 1
def is_pared1(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_area = image.shape[0] * image.shape[1]

    laplacian = cv2.Laplacian(blur, cv2.CV_64F).var()
    if laplacian < 100:
        textura = True

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (area > 0.7 * img_area) and textura:
            return True
    return False
        

def is_pared2(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_area = image.shape[0] * image.shape[1]

    for cnt in contours:
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w)/h
            if 1.3 < aspect_ratio < 2.5:
                return True
    return False