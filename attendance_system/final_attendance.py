import cv2
import pyttsx3
import pandas as pd
from datetime import datetime
from pyzbar.pyzbar import decode
import os

# 🔥 BASE PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Create recognizer FIRST
recognizer = cv2.face.LBPHFaceRecognizer_create()

# ✅ Load trained model
model_path = os.path.join(BASE_DIR, "trainer.yml")
if not os.path.exists(model_path):
    print("❌ trainer.yml not found. Run trainer.py first")
    exit()

recognizer.read(model_path)

# 🔊 Voice engine
engine = pyttsx3.init()
last_spoken = ""

# 👤 Face detector
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 📁 CSV setup
file_name = os.path.join(BASE_DIR, "attendance.csv")

try:
    df = pd.read_csv(file_name)
except:
    df = pd.DataFrame(columns=["StudentID", "Time"])

# 🎥 Camera (Windows fix)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Scan QR + Face to mark attendance")

while True:
    ret, frame = cam.read()
    if not ret:
        print("❌ Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    message = ""
    color = (255, 255, 255)

    # 🔍 QR Detection
    qr_id = None
    for barcode in decode(frame):
        qr_id = barcode.data.decode('utf-8')

        pts = barcode.polygon
        if len(pts) > 4:
            pts = pts[:4]

        for i in range(len(pts)):
            cv2.line(frame, pts[i], pts[(i + 1) % len(pts)], (0, 255, 0), 3)

        cv2.putText(frame, f"QR: {qr_id}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 👤 Face Detection
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        face_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 100:
            face_id = str(face_id)
            today = datetime.now().strftime("%Y-%m-%d")

            # 🔐 QR parsing
            if qr_id:
                parts = qr_id.split("_")
                if len(parts) == 3:
                    name, qr_student_id, qr_date = parts
                elif len(parts) == 2:
                    name, qr_student_id = parts
                    qr_date = today
                else:
                    qr_student_id = None
                    qr_date = None
                    name = "Unknown"
            else:
                qr_student_id = None
                qr_date = None
                name = "No QR"

            # ✅ STRICT MATCH
            if qr_student_id == face_id and qr_date == today:

                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if face_id not in df["StudentID"].values:
                    new_entry = {"StudentID": face_id, "Time": time_now}
                    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
                    df.to_csv(file_name, index=False)

                    message = f"Attendance marked for ID: {face_id}"
                    color = (0, 255, 0)

                    if last_spoken != "marked":
                        engine.say("Attendance marked")
                        engine.runAndWait()
                        last_spoken = "marked"

                else:
                    message = f"Already marked for ID: {face_id}"
                    color = (0, 0, 255)

                    if last_spoken != "already":
                        engine.say("Already marked")
                        engine.runAndWait()
                        last_spoken = "already"

                label = f"{name} ({face_id})"

            else:
                message = "QR + Face mismatch"
                color = (0, 0, 255)
                label = "Mismatch ❌"

                if last_spoken != "mismatch":
                    engine.say("Mismatch")
                    engine.runAndWait()
                    last_spoken = "mismatch"

        else:
            message = "Face not recognized"
            color = (0, 0, 255)
            label = "Unknown"

            if last_spoken != "unknown":
                engine.say("Face not recognized")
                engine.runAndWait()
                last_spoken = "unknown"

        # 🎯 Draw face box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # 📢 Show message
    cv2.putText(frame, message, (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Final Attendance System", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()