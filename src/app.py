import gradio as gr

# from media_processing import process_media
from image_processing import process_image

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
    file_input = gr.Image(type="filepath")
    process_button = gr.Button("Process File")
    output_image = gr.Image(type="pil", label="Processed Image", height=300, width=400)
    output_text = gr.Textbox(label="Detected Objects")

    process_button.click(
        process_image, inputs=[file_input], outputs=[output_image, output_text]
    )
    # file_output = gr.File()
    # upload_button = gr.UploadButton(
    #     "Click to Upload a File", file_types=["image", "video"], file_count="multiple"
    # )
    # upload_button.upload(upload_file, upload_button, file_output)

demo.launch()
