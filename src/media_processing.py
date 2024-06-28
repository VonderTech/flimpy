from image_processing_supervision import process_image
from video_processing_supervision import VideoProcessor

video_processor = VideoProcessor("yolov8n.pt")


def process_media(file_path):
    """
    Process the uploaded file, which can be an image or a video.
    """
    # Check the file type by extension
    file_type = file_path.split(".")[-1].lower()

    if file_type in ["jpg", "jpeg", "png"]:
        return process_image(file_path)
    elif file_type in ["mp4", "avi", "mov"]:
        return video_processor.process_video(file_path)
    else:
        return None, "Unsupported file type"
