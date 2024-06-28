import cv2
import supervision as sv
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def process_image(image_path):
    """
    Process the image, detect objects and return the it with detected objects
    highlighted.
    """
    image = cv2.imread(image_path)
    results = model(image)[0]
    detections = sv.Detections.from_ultralytics(results)

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = bounding_box_annotator.annotate(
        scene=image, detections=detections
    )
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections
    )

    return annotated_image, detections
