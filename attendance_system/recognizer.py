import cv2
import pandas as pd
from datetime import datetime

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

# Load face detector
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# CSV file setup
file_name = "attendance.csv"
try:
    df = pd.read_csv(file_name)
except:
    df = pd.DataFrame(columns=["StudentID", "Time"])

cam = cv2.VideoCapture(0)

print("Press ESC to exit")

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 100:
            student_id = str(id)
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # ✅ Correct indentation here
            if student_id not in df["StudentID"].values:
                new_entry = {"StudentID": student_id, "Time": time_now}
                df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
                df.to_csv(file_name, index=False)

            label = f"ID: {student_id}"
        else:
            label = "Unknown"

        # Draw rectangle
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.imshow('Face Recognition', img)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()