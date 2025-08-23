# 🚗 Real-time-Bangladeshi-Vehicle-License-Plate-Detection-and-Tracking
---

# ⏩ Video Explanation

⏩ Demo Video Link: [https://youtu.be/BMsZLLyWoKg](https://youtu.be/zjS3RVrQKiw)

⏩ Download the video here: [Explanation Video.mp4](EXPLANATION.mp4).

---

![Demo of License Plate Detection](assets/demoo.gif)

---

## 🚀 Project Overview
A **real-time license plate recognition (LPR)** system built with YOLO, EasyOCR, OpenCV, and Tkinter GUI.

This project allows you to detect vehicles from live webcam feed or image/video files, perform OCR on Bangla & English license plates, and save structured vehicle data in a JSON file.

The YOLO model is trained on the Bangladeshi Vehicle License Plate Dataset. **Kaggle Dataset:** [link](https://www.kaggle.com/datasets/sifatkhan69/bangladeshi-vehicle-license-plate/data)

- Detects **vehicles and their license plates** using a YOLO model.
- Extracts **Bangla and English** text from license plates using EasyOCR.
- Keeps track of **multiple vehicles** with ID assignment and bounding box tracking.
- Cleans **OCR results** and stores the top 3 most frequently recognized texts per vehicle.
- Draws **Unicode Bangla text** on frames for better visualization.
- Saves final vehicle data in a human-readable **JSON format**.

---

## 🧠 What Each File Does

- **main.py** → Entry point; launches the Tkinter GUI.
- **models.py** → Loads YOLO object detection model.
- **ocr.py** → Handles OCR for Bangla & English license plates.
- **iou.py** → Computes Intersection-over-Union (IoU) for bounding box tracking.
- **frame_processor.py** → Processes each frame, detects plates, assigns IDs, and annotates images.
- **json_utils.py** → Manages storing vehicle data in JSON format.
- **gui.py** → Tkinter interface for running live webcam or image/video file detection.
- **Bangla_Font.ttf** → Bengali Language Font.

---

## 🔄 Workflow

1. Start the application via main.py.
2. Select Live Webcam or Image/Video file.
3. **Vehicle Detection:** YOLO identifies vehicles and plates.
4. **OCR Extraction:** EasyOCR extracts license plate text in Bangla & English.
5. **ID Assignment:** Assigns a unique ID per vehicle and updates bounding boxes.
6. **Annotation:** Draws bounding boxes and Unicode text on frames.
7. **Data Storage:** Saves results as structured JSON with top-recognized texts.

---

## ⚙️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Make sure you have a Bangla Unicode font **(e.g., Bangla_Font.ttf)** in the project directory.
3. Place your trained YOLO model in the models/ folder as best.pt.
4. Run the GUI:
   ```bash
   python main.py
5. In the UI:
   - Click **Live Webcam** to detect plates in real-time.
   - Click **Select Image/Video** to choose files for processing.
   - Press **Q** to exit webcam or video playback.
6. After processing, a vehicle_data.json file will be saved with structured vehicle IDs, bounding boxes, and top OCR texts.
