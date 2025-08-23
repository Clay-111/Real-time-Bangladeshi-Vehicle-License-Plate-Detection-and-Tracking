import easyocr
import re

# EasyOCR readers
reader_en = easyocr.Reader(['en'], gpu=True)
reader_bn = easyocr.Reader(['bn'], gpu=True)

def detect_plate_script(plate_img):
    result_en = reader_en.readtext(plate_img, detail=1)
    result_bn = reader_bn.readtext(plate_img, detail=1)
    
    len_en = sum(len(t[1]) for t in result_en) if result_en else 0
    len_bn = sum(len(t[1]) for t in result_bn) if result_bn else 0
    
    if len_bn > len_en:
        result = result_bn
        script = 'bn'
    else:
        result = result_en
        script = 'en'
    
    result_sorted = sorted(result, key=lambda x: (x[0][0][1], x[0][0][0]))
    
    plate_text_list = []
    for t in result_sorted:
        clean_text = re.sub(r'[^অ-হক-হা-ৌ০-৯A-Z0-9\- ]', '', t[1])
        if clean_text:
            plate_text_list.append(clean_text)
    
    plate_text = ' '.join(plate_text_list)
    return script, plate_text
