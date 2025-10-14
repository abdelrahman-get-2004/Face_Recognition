import os
from PIL import Image

DATA_PATH = "Desktop/Face_recognition/DATA1"
TARGET_SIZE = (480, 480)

for person in os.listdir(DATA_PATH):
    person_path = os.path.join(DATA_PATH, person)
    if not os.path.isdir(person_path):
        continue

    for file in os.listdir(person_path):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(person_path, file)
            try:
                img = Image.open(path).convert("RGB")
                img = img.resize(TARGET_SIZE)
                img.save(path)
                print(f"[OK] Resized {file} in {person}")
            except Exception as e:
                print(f"[ERROR] {file}: {e}")
