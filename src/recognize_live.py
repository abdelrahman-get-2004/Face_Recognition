import cv2 as cv
import pickle
import face_recognition


MODEL_PATH = "Desktop/Face_recognition/models/face_encodings.pkl"

with open(MODEL_PATH, "rb") as f:
    data = pickle.load(f)

print(f"[INFO] Loaded {len(data['encodings'])} encodings for {len(set(data['names']))} people.")

video = cv.VideoCapture(1, cv.CAP_AVFOUNDATION)

if not video.isOpened():
    # If the default index fails, try 1 with the backend
    video = cv.VideoCapture(0, cv.CAP_AVFOUNDATION)

if not video.isOpened():
    print("❌ ERROR: Could not open camera with AVFoundation backend.")
    exit()

# Add a slight delay (still good practice)
cv.waitKey(100) 


while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for (top, right, bottom, left), enc in zip(locations, encodings):
        matches = face_recognition.compare_faces(data["encodings"], enc, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            idx = matches.index(True)
            name = data["names"][idx]

        cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv.putText(frame, name, (left, top - 10),
                    cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv.imshow("Face Recognition", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv.destroyAllWindows()