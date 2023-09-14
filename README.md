# Mobile Document Scanner

The Mobile Document Scanner is a Python project that utilizes computer vision techniques to scan documents and convert them into a digital format. This project provides a convenient and easy-to-use tool for capturing high-quality images of documents, receipts, or any other printed material using a mobile device's camera.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Folder Structure](#folder-structure)
- [Acknowledgments](#acknowledgments)

## Features

- **Automatic Document Detection:** The scanner automatically detects the edges of the document in the image.
- **Perspective Correction:** It applies a four-point perspective transform to straighten and align the document.
- **Image Enhancement:** Various image processing techniques are used to enhance the scanned document's quality.
- **Export Options:** The scanned document can be saved in various formats such as PDF, JPG, or PNG.
- **Simple User Interface:** The user-friendly interface makes it easy for anyone to use the scanner with ease.

## Installation

1. Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/amirshq/Mobile-Document-Scanner.git
```

2. Navigate to the project directory:

```shell
cd mobile-document-scanner
```

3. Install the required Python libraries using pip:

```shell
pip install -r requirements.txt
```

4. Run the scanner:

```shell
python scan.py
```

## How to Use

1. Launch the application and grant camera permissions when prompted.
2. Hold the mobile device over the document you want to scan. Make sure all four corners of the document are visible on the screen.
3. The scanner will automatically detect the document's edges and apply perspective correction.
4. Tap the capture button to save the scanned document.
5. Choose the desired export format (PDF, JPG, or PNG).
6. The scanned document will be saved to the device's storage in the selected format.

## Folder Structure

- **_README.md_**: The main documentation file for your project.
- **_Update README .md_**: A commit indicating an update to the project's README file.
- **_WholeFoodReceipt .jpg_**: An example image file of a receipt (JPEG format).
- **_fourpointtransform .py_**: A Python script for applying a four-point perspective transform to images.
- **_image.jpg_**: An example image file (JPEG format).
- **_mobile document Scanner.html_**: An HTML file, possibly for a web-based component of your project.
- **_scan .py_**: The main Python script responsible for running the document scanner.
- **_Update scan .py_**: A commit indicating an update to the `scan.py` script.
- **_transform.pyv_**: A Python script related to image transformation.
- **_Update transform .py_**: A commit indicating an update to the `transform.py` script.
- **_transform_example.py_**: A Python script demonstrating image transformation.

## Acknowledgments

- (Mention any libraries, tools, or tutorials you used or were inspired by.)
- (Give credit to any contributors or authors of external code used in the project.)
