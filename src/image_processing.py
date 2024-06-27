import torch
from PIL import Image, ImageDraw, ImageFont
from transformers import AutoImageProcessor, AutoModelForObjectDetection

# Load the model and the feature extractor
image_processor = AutoImageProcessor.from_pretrained("hustvl/yolos-tiny")
model = AutoModelForObjectDetection.from_pretrained("hustvl/yolos-tiny")


def process_image(image_path):
    """
    Process the image, detect objects and return the it with detected objects
    highlighted.
    """
    image = Image.open(image_path)
    # Preprocess image and prepare for the model
    inputs = image_processor(images=image, return_tensors="pt")

    # Forward pass, get predictions
    outputs = model(**inputs)

    # convert outputs (bounding boxes and class logits) to COCO API
    target_sizes = torch.tensor([image.size[::-1]])
    results = image_processor.post_process_object_detection(
        outputs, threshold=0.9, target_sizes=target_sizes
    )[0]

    # Initialize drawing context
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    detected_objects = []
    # Draw results
    for score, label, box in zip(
        results["scores"], results["labels"], results["boxes"]
    ):
        box = [round(i, 2) for i in box.tolist()]
        draw.rectangle(((box[0], box[1]), (box[2], box[3])), outline="red", width=3)
        draw.text(
            (box[0], box[1]),
            f"{model.config.id2label[label.item()]}: {round(score.item(), 3)}",
            fill="red",
            font=font,
        )
        detected_objects.append(
            f"{model.config.id2label[label.item()]}: {round(score.item(), 3)} at {box}"
        )

    detected_objects.append(
        f"{model.config.id2label[label.item()]}: {round(score.item(), 3)} at {box}"
    )

    return image, detected_objects
