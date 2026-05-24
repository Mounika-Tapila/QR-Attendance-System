import cv2
import os
import sys
import subprocess

# 🔥 BASE PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "dataset")

# 📁 Create dataset folder
os.makedirs(dataset_path, exist_ok=True)

# 🎯 GET STUDENT ID
if len(sys.argv) > 1:
    student_id = sys.argv[1]
else:
    student_id = input("Enter Student ID: ")

print(f"Starting capture for ID: {student_id}")

# 🎥 Camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 👤 Face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0

while True:
    ret, img = cam.read()
    if not ret:
        print("Camera not working ❌")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1

        face_img = gray[y:y+h, x:x+w]

        # 💾 Save face
        file_path = os.path.join(dataset_path, f"User.{student_id}.{count}.jpg")
        cv2.imwrite(file_path, face_img)

        # 🟦 Draw rectangle
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.putText(img, f"Capturing {count}/50", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('Face Capture', img)

    # 🎯 CAPTURE MORE IMAGES (IMPORTANT)
    if count >= 50:
        break

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

print("✅ Dataset collection complete")

# 🔥 AUTO TRAIN MODEL (USE VENV PYTHON)
print("⚡ Training started...")

trainer_path = os.path.join(BASE_DIR, "trainer.py")

# ✅ Use SAME python (very important)
python_path = sys.executable

subprocess.call([python_path, trainer_path])

print("✅ Training completed successfully!")