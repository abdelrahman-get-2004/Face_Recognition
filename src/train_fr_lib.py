import os
import pickle
import face_recognition

DATA_PATH = "Desktop/Face_recognition/DATA1"
MODEL_PATH = "../models/face_encodings.pkl"

encodings = []
names = []

print("[INFO] Starting face encoding...")

for person in os.listdir(DATA_PATH):
    person_path = os.path.join(DATA_PATH, person)
    if not os.path.isdir(person_path):
        continue

    for image_file in os.listdir(person_path):
        if not image_file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(person_path, image_file)
        image = face_recognition.load_image_file(img_path)
        face_locations = face_recognition.face_locations(image)
        face_encs = face_recognition.face_encodings(image, face_locations)

        if len(face_encs) > 0:
            encodings.append(face_encs[0])
            names.append(person)

print(f"[INFO] Encoded {len(encodings)} faces from {len(set(names))} people.")

data = {"encodings": encodings, "names": names}
os.makedirs("/Users/abdelrahman/Desktop/Face_recognition/models", exist_ok=True)
with open("/Users/abdelrahman/Desktop/Face_recognition/models/face_encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print(f"[INFO] Model saved to {MODEL_PATH}")
