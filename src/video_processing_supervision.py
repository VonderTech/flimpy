import os

import numpy as np
import supervision as sv
import torch
from ultralytics import YOLO


class VideoProcessor:
    def __init__(self, model_path, confidence_threshold=0.5):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()
        self.box_annotator = sv.BoundingBoxAnnotator()
        self.label_annotator = sv.LabelAnnotator()
        self.detections_list = []
        # Initialize an empty dictionary to store detections
        self.detections_map = {}
        self.confidence_threshold = confidence_threshold

    def callback(self, frame: np.ndarray, _: int) -> np.ndarray:
        results = self.model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = self.tracker.update_with_detections(detections)
        labels = []

        for class_id, tracker_id, confidence in zip(
            detections.class_id, detections.tracker_id, detections.confidence
        ):
            confidence = confidence.item()
            if confidence >= self.confidence_threshold:
                if (
                    tracker_id not in self.detections_map
                    or confidence > self.detections_map[tracker_id]["confidence"]
                ):
                    self.detections_map[tracker_id] = {
                        "class": results.names[class_id],
                        "confidence": confidence,
                    }
            labels.append(f"#{tracker_id} {results.names[class_id]} {confidence:.2f}")

        # labels = [
        #     f"#{tracker_id} {results.names[class_id]} {confidence:.2f}"
        #     for class_id, tracker_id, confidence in zip(
        #         detections.class_id, detections.tracker_id, detections.confidence
        #     )
        # ]

        self.detections_list.append(detections)

        annotated_frame = self.box_annotator.annotate(
            frame.copy(), detections=detections
        )
        return self.label_annotator.annotate(
            annotated_frame,
            detections=detections,
            labels=labels,
        )

    def process_video(self, file_path):
        self.detections_list = []  # Reset the detections list for a new video

        # Check if CUDA is available and set the device
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {device}")

        # Ensure the output directory exists
        output_dir = "output_videos"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "processed_video.mp4")

        sv.process_video(
            source_path=file_path,
            target_path=output_path,
            callback=self.callback,
        )

        print("Video processing complete")
        print(f"Annotated video saved to: {output_path}")
        print("Detections map:", self.detections_map)

        return output_path, self.detections_map


# # Example usage
# video_processor = VideoProcessor("yolov8n.pt")
# output_video_path, detections_list = video_processor.process_video(
#     "path_to_your_video.mp4"
# )
# print(f"Annotated video saved to: {output_video_path}")
# print("Detections list:", detections_list)
