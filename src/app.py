import gradio as gr

# from media_processing import process_media
# from image_processing import process_image
from media_processing import process_media

# # Define the Gradio interface
# interface = gr.Interface(
#     fn=process_media,
#     # inputs=gr.File(
#     #     file_types=["image", "video"],
#     #     label="Upload an image or a video",
#     #     file_count="single",
#     # ),
#     inputs=gr.Image(label="Upload an image or a video"),
#     outputs=gr.Image(label="Processed Image/Video"),
#     title="Yolo Object Detection",
#     description="Upload an image or a video to detect its objects.",
# )


def upload_file(filepath):
    """
    Process an uploaded file which can be an image or a video.
    """
    if filepath is None:
        return "Please upload a file."

    return filepath


with gr.Blocks() as demo:
    with gr.Tab("Image"):
        image_input = gr.Image(type="filepath", label="Upload an Image")
        process_image_button = gr.Button("Process Image")
        output_image = gr.Image(
            type="filepath", label="Processed Image", height=300, width=400
        )
        output_image_text = gr.Textbox(label="Detected Objects in Image")

        process_image_button.click(
            process_media,
            inputs=[image_input],
            outputs=[output_image, output_image_text],
        )

    with gr.Tab("Video"):
        video_input = gr.Video(label="Upload a Video")
        process_video_button = gr.Button("Process Video")
        output_video = gr.Video(label="Processed Video", height=300, width=400)
        output_video_text = gr.Textbox(label="Detected Objects in Video")

        process_video_button.click(
            process_media,
            inputs=[video_input],
            outputs=[output_video, output_video_text],
        )

demo.launch()
