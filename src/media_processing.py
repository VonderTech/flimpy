from video_processing import process_video
from image_processing import process_image


def process_media(file_info):
    """
    Process an uploaded file which can be an image or a video.
    """
    filepath, file_type = file_info
    if file_type.startswith("image"):
        # Process image
        image = process_image(filepath)
        return image
    elif file_type.startswith("video"):
        # Process video
        video = process_video(filepath)
        return video
    else:
        return "Unsupported file type"
