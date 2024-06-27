import cv2
import torch
import numpy
from transformers import YolosForObjectDetection
from PIL import Image, ImageDraw, ImageFont

# Load the YOLOv8 model
model = YolosForObjectDetection.from_pretrained("hustvl/yolos-tiny")
model.eval()


def process_video(video_path):
    """
    Process the uploaded video, detect objects and return the video with detected objects highlighted.
    """
    cap = cv2.VideoCapture(video_path)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Convert the frame to PIL Image
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            inputs = model.feature_extractor(images=image, return_tensors="pt")
            outputs = model(**inputs)
            # Draw boxes on the frame
            draw = ImageDraw.Draw(image)
            for i in range(len(outputs["labels"])):
                box = outputs["boxes"][i].numpy()
                label = outputs["labels"][i]
                score = outputs["scores"][i]
                if score > 0.5:  # Only display boxes above a certain threshold
                    draw.rectangle(
                        [(box[0], box[1]), (box[2], box[3])], outline="red", width=3
                    )
                    draw.text(
                        (box[0], box[1]),
                        f"{model.config.id2label[label.item()]}: {score:.2f}",
                        fill="red",
                    )
            # Convert back to BGR for OpenCV
            frame = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
            out.write(frame)
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    return "output.mp4"
