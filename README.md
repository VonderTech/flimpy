# Flimpy - Object Detection

![Build Status](https://github.com/VonderTech/flimpy/actions/workflows/gradio-app.yml/badge.svg)
![Dependabot Status](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/bc2eb32794604406a7141e5443545bb4)](https://app.codacy.com/gh/VonderTech/flimpy/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
![GitHub last commit](https://img.shields.io/github/last-commit/VonderTech/flimpy)
![GitHub issues](https://img.shields.io/github/issues/VonderTech/flimpy)
[![License: MIT][license_badge]][license_link]

Flimpy is a simple web application for object detection using YOLOv8, implemented with Gradio for the user interface. Users can upload images or videos, and the app will process them to detect and highlight objects.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Description

Flimpy leverages the YOLOv8 model for object detection, allowing users to upload images or videos and see detected objects highlighted with bounding boxes and labels. The user interface is built with Gradio, making it simple and accessible via a web browser.

## Installation

### Prerequisites

- Python 3.8 or higher
- Poetry for dependency management

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/flimpy.git
    cd flimpy
    ```

2. **Install dependencies**

    Make sure you have Poetry installed. If not, you can install it from [here](https://python-poetry.org/docs/#installation).

    ```bash
    poetry install
    ```

3. **Download the YOLOv8 model**

    The model is automatically downloaded when you run the application for the first time.

## Usage

1. **Activate the virtual environment**

    ```bash
    poetry shell
    ```

2. **Run the application**

    ```bash
    python app.py
    ```

3. **Open the Gradio interface**

    Open your web browser and navigate to the URL provided by Gradio (usually `http://127.0.0.1:7860/`).

4. **Upload an image or video**

    - Upload an image or video file.
    - Click the "Process File" button.
    - View the processed image or video with detected objects highlighted.

## Features

- **Image and Video Processing**: Supports both image and video file uploads.
- **Object Detection**: Uses YOLOv8 for high-accuracy object detection.
- **User-Friendly Interface**: Built with Gradio for a simple and intuitive user experience.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[license_badge]: https://img.shields.io/badge/license-MIT-blue.svg
[license_link]: https://opensource.org/licenses/MIT
