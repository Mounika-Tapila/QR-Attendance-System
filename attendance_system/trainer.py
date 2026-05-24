import cv2
import numpy as np
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "dataset")
model_path = os.path.join(BASE_DIR, "trainer.yml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        # 🔥 FIX: Extract correct ID
        student_id = os.path.split(imagePath)[-1].split(".")[1]

        try:
            id = int(student_id)
        except:
            continue

        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids


faces, ids = getImagesAndLabels(dataset_path)

if len(faces) == 0:
    print("❌ No faces found. Capture dataset again.")
    exit()

recognizer.train(faces, np.array(ids))
recognizer.write(model_path)

print("✅ Model trained successfully")