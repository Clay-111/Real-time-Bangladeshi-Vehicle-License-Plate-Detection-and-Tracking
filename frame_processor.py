import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from ocr import detect_plate_script
from iou import iou
from json_utils import all_files_vehicle_data, save_vehicle_data

def put_unicode_text(img, text, position, font_path="Bangla_Font.ttf", font_size=32, color=(0,255,0)):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def process_frame(frame, vehicle_data, vehicle_id_counter, model):
    results = model.predict(source=frame, verbose=False)
    current_frame_boxes = []

    for result in results:
        if not hasattr(result, 'boxes') or len(result.boxes) == 0:
            continue
        for box in result.boxes.xyxy.cpu().numpy():
            x1, y1, x2, y2 = map(int, box)
            plate_img = frame[y1:y2, x1:x2]

            script, plate_text = detect_plate_script(plate_img)
            plate_text = plate_text.strip()
            
            if plate_text == "":
                continue

            matched_id = None
            for vid, vinfo in vehicle_data.items():
                if iou(vinfo['bbox'], [x1,y1,x2,y2]) > 0.3:
                    matched_id = vid
                    break

            if matched_id is None:
                matched_id = str(vehicle_id_counter)
                vehicle_data[matched_id] = {'bbox':[x1,y1,x2,y2], 'texts':[plate_text]}
                vehicle_id_counter += 1
            else:
                prev_box = vehicle_data[matched_id]['bbox']
                new_box = [
                    int((prev_box[0]+x1)/2),
                    int((prev_box[1]+y1)/2),
                    int((prev_box[2]+x2)/2),
                    int((prev_box[3]+y2)/2)
                ]
                vehicle_data[matched_id]['bbox'] = new_box
                vehicle_data[matched_id]['texts'].append(plate_text)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            frame = put_unicode_text(frame, plate_text, (x1, max(0, y1-40)))
            print(f"Vehicle ID {matched_id} ({script}): {plate_text}")
            current_frame_boxes.append([x1,y1,x2,y2])

    return frame, vehicle_id_counter
