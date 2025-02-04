
# Telegram Data Scraping and Object Detection Pipeline

## Overview
This project scrapes data from public Telegram channels, cleans and transforms it, performs object detection using YOLO, and exposes the data via a FastAPI service.

---
## Features
✅ Scrape Telegram data using **Telethon**  
✅ Clean and transform data using **Pandas & DBT**  
✅ Perform object detection using **YOLOv5**  
✅ Expose collected data via **FastAPI**  

---
## Setup & Installation
### 1️⃣ Install Dependencies
```bash
pip install telethon pandas sqlalchemy dbt-core opencv-python torch torchvision fastapi uvicorn
```

---
## Task 1 - Data Scraping
### Extract data from Telegram channels:
- **Libraries Used**: `Telethon`
- **Steps**:
  1. Use Telethon API to scrape data from Telegram.
  2. Store raw data in a local database.
  3. Implement logging for monitoring.

---
## Task 2 - Data Cleaning & Transformation
### Cleaning Steps:
- Remove duplicates
- Handle missing values
- Standardize formats

### DBT Transformation:
```bash
pip install dbt-postgres  # Install DBT
cd my_project
```
Run transformations:
```bash
dbt run
dbt test
```

---
## Task 3 - Object Detection using YOLO
### Steps:
1. Clone YOLOv5 and install dependencies:
```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```
2. Process images:
```python
import torch
model = torch.hub.load("ultralytics/yolov5", "yolov5s")
results = model("images/sample.jpg")
results.show()
```

---
## Task 4 - Exposing Data via FastAPI
### Steps:
1. Install FastAPI and Uvicorn:
```bash
pip install fastapi uvicorn sqlalchemy
```
2. Create API structure and models:
```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "API is running"}
```
3. Run the server:
```bash
uvicorn main:app --reload
```
=======

# Data Scraping and Collection Pipeline

This repository contains the instructions for scraping and collecting data from specific Telegram channels related to Ethiopian medical businesses and collecting images for object detection. The goal is to build a pipeline to extract messages and media (images) from public Telegram channels and store them for further processing.

## Task Overview

- **Scrape Telegram Channels**: Use the Telegram API to extract text messages and media (such as images) from selected public Telegram channels.
- **Data Storage**: Save raw data (text messages and images) to your local or cloud storage for further processing.
- **Monitoring and Logging**: Implement logging to track the scraping process, capture errors, and monitor progress.

## Telegram Channels to Scrape

- [DoctorsET](https://t.me/DoctorsET)
- [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
- [Yetenaweg](https://t.me/yetenaweg)
- [EAHCI](https://t.me/EAHCI)

For additional channels, you can explore [ET TGStat](https://et.tgstat.com/medicine).

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x
- Google Colab (for easy setup and running)
- Telegram API credentials (API ID and API Hash from [my.telegram.org](https://my.telegram.org/auth))

## Installation

1. **Install Required Packages**:  
   Use the `Telethon` library for scraping data from Telegram. You can install it using pip in your Colab environment:

   ```bash
   !pip install telethon
   ```

2. **Mount Google Drive**:  
   If you're using Google Colab, you can mount Google Drive to access and store files:

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. **Extract ZIP File (If needed)**:  
   If you're working with a ZIP file, you can extract it to your desired directory:

   ```python
   import zipfile

   # Replace with your actual zip file path
   zip_file_path = '/content/drive/MyDrive/path_to_zip_file.zip'
   extraction_folder = '/content/drive/MyDrive/unzipped_files/'

   with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
       zip_ref.extractall(extraction_folder)

   print(f"Files extracted to {extraction_folder}")
   ```

## Usage

1. **Set Up Telethon for Telegram Scraping**:  
   After installing the necessary packages, you will need to set up **Telethon** by adding your **API ID** and **API Hash** from your [Telegram Developer Account](https://my.telegram.org/auth). These credentials are required for connecting to Telegram's API.

2. **Scrape Telegram Channels**:  
   Use the functions to scrape messages and images from the specified Telegram channels. This process will collect text and media (images) from the channels and save them to your Google Drive or local storage for further processing.

3. **Data Storage**:  
   - **Text Data**: All scraped text messages will be saved in a text file (`scraped_data.txt`).
   - **Images**: Images and media files from the channels will be stored in the specified folder (e.g., `/content/drive/MyDrive/images/`).

## Monitoring and Logging

To monitor the scraping process, you can implement logging. This will allow you to track progress, capture any errors, and log important milestones throughout the scraping process.

- Logs will help you identify any issues such as API connection failures or message scraping limits.
- You can log both **informational** and **error** messages to help monitor the pipeline effectively.

## Notes

- **Telegram API Credentials**: Make sure you generate and provide your **API ID** and **API Hash** from the [Telegram Developer Portal](https://my.telegram.org/auth).
- **Rate Limiting**: Telegram may rate-limit your requests if too many messages are scraped in a short period. Be sure to follow a reasonable scraping pace.
- **Storage**: Ensure your Google Drive or local storage has enough space for the scraped data, especially when collecting media files like images.

## Troubleshooting

- **API Credentials**: Double-check your API ID and API Hash if you encounter authentication issues.
- **Telegram Limits**: If Telegram blocks or restricts your scraping attempts, try reducing the scraping frequency or use different methods for pagination.
- **Storage**: If you run out of space when saving images, clean up your storage or consider using cloud storage solutions.


