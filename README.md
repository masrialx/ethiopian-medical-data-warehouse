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
