# VPO_Project - Image Analysis with YOLOv5

## Description
VPO_Project is a simple web application that performs image analysis using the YOLOv5 model. The application allows users to upload an image via a web interface and then displays the detected objects in the image along with their confidence levels.

## Project Structure
The project is organized as follows:

VPO_Project/
│
├── static/
│   ├── css/
│   │   └── style.css           # stylesheet for the HTML page
│   └── js/
│       └── script.js           # JavaScript for handling interface interaction
│
├── templates/
│   └── index.html              # Main HTML page
│
├── visionPatOrdinateurCam.py   # Python script for computer vision with YOLOv5
│
├── app.py                      # Main script that runs the Flask server
│
├── requirements.txt            # List of Python project dependencies
│
└── README.md                   # Project documentation

## Prerequisites
Ensure that you have Python 3.9 or higher installed, along with the following packages:

- Flask
- torch
- torchvision
- Pillow
- OpenCV (cv2)

You can install the dependencies using the following command:

pip install -r requirements.txt

## Installation
    Navigate to the project directory:
  cd VPO_Project

  Install the required dependencies:
  pip install -r requirements.txt

## Usage
  Open your web browser and go to the following address: http://127.0.0.1:5000

Upload an image using the web interface and click "Analyze." The detected objects in the image will be displayed along with their confidence levels.

## Important Files
1. app.py
This is the main script that runs the Flask application. It handles the routes, including the main page and the /analyze route, which receives the uploaded image and returns the analysis results.

2. visionParOrdinateurCam.py
This file contains the computer vision logic. It uses the YOLOv5 model to detect objects in images.

3. index.html
The HTML file that contains the structure of the web page. It includes a form to upload images, a button to start the analysis, and a section to display the results.

4. style.css
The CSS file that styles the HTML page. It is included via the static/css/ folder.

5. script.js
The JavaScript file that manages user interaction. It processes the uploaded image, sends a POST request to the Flask server, and displays the results returned by the server.

## Warnings
This application uses a Flask server in development mode. To deploy the application in production, please use a WSGI server such as Gunicorn or uWSGI.

## Licence
This project is licensed under the MIT License. See the LICENSE file for more details.

## Conclusion
This documentation provides all the information needed to install, configure, and use the VPO_Project. Be sure to follow the steps outlined to ensure the application functions correctly.