# Netra – Real-time Pothole Detection System

Netra is a real-time pothole detection web application built using Streamlit and powered by the YOLOv8 segmentation model. It processes videos, live streams, and stored sessions to detect potholes accurately and displays the detected potholes' locations interactively on a map.

## Features
- **YOLOv8 Segmentation Model** for precise pothole detection.
- Supports **real-time video streams** and **video file inputs** for flexible usage.
- **Interactive Map View** using Folium to visualize pothole locations.
- **Session Management** for storing local data in `data.pkl` or optionally using AWS DynamoDB for cloud storage and retrieval.
- Multi-page Streamlit UI, including:
  - Home page for live detection.
  - Session Details page to review recorded sessions.
  - About page describing the system.
- Optional **AWS Integration** via `cloudDyn.py` for cloud data management.

## Project Structure
```Netra/
  app.py                    # Main Streamlit application
  cloudDyn.py               # Utilities for AWS DynamoDB integration
  helper.py                 # Contains model loading and detection functions
  settings.py               # Configuration constants
  requirements.txt          # All Python dependencies
  data.pkl                  # Sample local session data

  pages/
    1_🗃️_Session_Details.py         # Page for local session details
    2_🧛_About.py                   # About page
    AWS version/
      1_🗃️_Session_Details(AWS).py # AWS-based session details page

  weights/
    best.pt                  # Custom-trained YOLOv8 model weights
    yolov8s-seg.pt           # YOLOv8 base segmentation model weights
```

## Installation

1. Clone the repository:

git clone https://github.com/shrey423/Netra.git
cd Netra
2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Ensure the YOLO model weights are placed in the `weights/` directory:
- `best.pt` (custom-trained model weights)
- `yolov8s-seg.pt` (base YOLOv8 segmentation model weights)

## Usage

Run the Streamlit app:
streamlit run app.py

Access the application in your browser at:
http://localhost:8501

## AWS Integration (Optional)

To enable cloud storage and retrieval of session data via AWS DynamoDB:

1. Configure AWS credentials on your machine:
aws configure

2. Verify or update the DynamoDB table name and schema in `cloudDyn.py`.

3. Use the AWS-specific session details page located at:
pages/AWS version/1_🗃️_Session_Details(AWS).py

## How It Works

- **Detection:** The YOLOv8 model, loaded via `helper.py`, processes video frames in real-time to segment and detect potholes.
- **Display:** Detection results are annotated on video frames and shown live within the Streamlit app.
- **Data Logging:** Pothole count, GPS locations, and timestamps are logged locally (`data.pkl`) or optionally into AWS DynamoDB.
- **Review:** Historical sessions can be reviewed on an interactive map thanks to Folium integration.

## Requirements

Key dependencies include:
- streamlit
- ultralytics (for YOLOv8)
- opencv-python
- pandas
- numpy
- folium
- boto3 (for AWS support)
- streamlit-folium

Install all dependencies from:
pip install -r requirements.txt

This system offers an effective, real-time pothole detection solution with interactive visualization and robust session management, suitable for road maintenance and smart city applications. The optional cloud integration enables scalable data storage and retrieval in production scenarios.
