# 🧠 Face Recognition Project

This project implements a **facial recognition system** using Python and the `face_recognition` library.  
It detects and identifies faces from known individuals stored in local folders.

---

## 📂 Project Structure
Face_Recognition/
├── src/ # Python source files
├── models/ # Saved encodings (not uploaded)
└── data1/ (not uploaded)


---

## ⚙️ Installation
Clone the repository:
```bash
git clone https://github.com/<yourusername>/Face_Recognition.git
cd Face_Recognition


Create a virtual environment and install dependencies:

python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt

🚀 Usage

Resize and preprocess images:

python src/preprocess_images.py


Train and save face encodings:

python src/train_fr_lib.py


Recognize faces in a new image:

python src/recognize_faces.py

🧠 Technologies Used

Python 3.9+

face_recognition & dlib

OpenCV

NumPy, Pillow, Matplotlib

👨‍💻 Author

Abdelrahman Abdelmagid
M1 SysCom – Sorbonne Université
📧 abdelmagid3007@gmail.com
