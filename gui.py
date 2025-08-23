import cv2
from tkinter import Tk, Button, filedialog
import os
from frame_processor import process_frame
from models import model
from json_utils import all_files_vehicle_data, save_vehicle_data

def run_webcam():
    vehicle_data = {}
    vehicle_id_counter = 1
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        return
    cv2.namedWindow("License Plate Recognition", cv2.WINDOW_NORMAL)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame, vehicle_id_counter = process_frame(frame, vehicle_data, vehicle_id_counter, model)
        cv2.imshow("License Plate Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    all_files_vehicle_data["webcam"] = vehicle_data
    save_vehicle_data()

def run_image_video():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Media files","*.jpg *.jpeg *.png *.mp4 *.avi *.mov")])
    if not file_path:
        return

    vehicle_data = {}
    vehicle_id_counter = 1
    file_key = os.path.basename(file_path)

    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        frame = cv2.imread(file_path)
        frame, vehicle_id_counter = process_frame(frame, vehicle_data, vehicle_id_counter, model)
        cv2.imshow("License Plate Recognition", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cap = cv2.VideoCapture(file_path)
        cv2.namedWindow("License Plate Recognition", cv2.WINDOW_NORMAL)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame, vehicle_id_counter = process_frame(frame, vehicle_data, vehicle_id_counter, model)
            cv2.imshow("License Plate Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    all_files_vehicle_data[file_key] = vehicle_data
    save_vehicle_data()

def start_gui():
    root = Tk()
    root.title("License Plate Recognition")
    root.geometry("400x200")

    btn_webcam = Button(root, text="Live Webcam", command=run_webcam, width=25, height=2)
    btn_webcam.pack(pady=20)

    btn_file = Button(root, text="Select Image/Video", command=run_image_video, width=25, height=2)
    btn_file.pack(pady=20)

    root.mainloop()
