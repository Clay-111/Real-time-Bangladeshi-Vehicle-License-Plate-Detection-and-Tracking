import json
import re

all_files_vehicle_data = {}

def save_json_inline_arrays(data, filename):
    text = json.dumps(data, indent=4, ensure_ascii=False)
    text = re.sub(
        r"\[\s+([^\[\]]*?)\s+\]",
        lambda m: "[" + " ".join(m.group(1).split()) + "]",
        text,
        flags=re.S
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def save_vehicle_data():
    final_data = {}
    for file_name, vehicle_data in all_files_vehicle_data.items():
        file_dict = {}
        for vid, vinfo in vehicle_data.items():
            texts = vinfo['texts']
            freq = {}
            for t in texts:
                freq[t] = freq.get(t, 0) + 1
            top3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
            top3_texts = [t[0] for t in top3]
            file_dict[vid] = {
                "bbox": vinfo['bbox'],
                "texts": top3_texts
            }
        final_data[file_name] = file_dict

    save_json_inline_arrays(final_data, "vehicle_data.json")
    print("Saved vehicle_data.json")
