<h1 align="center">📸 QR + Face Based Attendance System</h1>

<p align="center">
  Smart Attendance System using QR Code + Face Recognition + Flask
</p>

---

## 🔥 Project Overview

This project is a **Smart Attendance Management System** that uses:

- 📷 Face Recognition (OpenCV)
- 🔳 QR Code Verification
- 🌐 Flask Web Application
- 📊 CSV-based Attendance Storage

It ensures **secure attendance** by matching both:
✔ Face ID  
✔ QR Code (with date validation)

---

## ✨ Features

- ✅ QR Code Generation for Students
- ✅ Face Recognition Authentication
- ✅ QR + Face Matching (Anti-Proxy)
- ✅ Admin Panel (Teacher Dashboard)
- ✅ Student Registration (Auto Dataset + Training)
- ✅ Real-time Attendance Marking
- ✅ Attendance Records (CSV + Web View)
- ✅ Voice Feedback (pyttsx3)

---

## 🧠 Tech Stack

- Python
- OpenCV (`cv2`)
- Flask
- Pandas
- Pyzbar (QR Scanner)
- pyttsx3 (Voice)
- HTML, CSS (Frontend)

---

## 📂 Project Structure

QR-Attendance-System/
│
├── attendance_system/
│ ├── dataset/
│ ├── trainer.yml
│ ├── final_attendance.py
│ ├── trainer.py
│ └── dataset_creator.py
│
├── attendance_web/
│ ├── templates/
│ │ ├── index.html
│ │ ├── admin_panel.html
│ │ ├── register.html
│ │ └── attendance.html
│ └── app.py
│
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/Mounika-Tapila/QR-Attendance-System.git
cd QR-Attendance-System

---

### 2️⃣ Create Virtual Environment

cd attendance_system
python -m venv venv
venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install opencv-contrib-python pyttsx3 pandas pyzbar pillow flask qrcode

---

### 4️⃣ Run Flask App

cd ../attendance_web
python app.py

Open browser:

http://127.0.0.1:5000

---

## 🔐 Login Credentials

Username: admin
Password: admin123

---

## 🧑‍🏫 Admin Panel Features

- ➕ Register New Student
- 📸 Auto Face Dataset Collection
- ⚡ Auto Model Training
- 🔳 Generate QR Code
- 📊 View Attendance Records

---

## 🧪 How It Works

1. Register student → captures face images
2. Model is trained automatically
3. QR Code is generated (Name + ID + Date)
4. During attendance:
   - Face is recognized
   - QR is scanned
   - Both must match ✅
5. Attendance is stored in CSV

---

## 📸 Screenshots

(Add your project screenshots here)

---

## 🚀 Future Improvements

- 🔐 Face Recognition Accuracy Boost (Deep Learning)
- 📍 Geo-fencing for attendance
- ☁️ Cloud Database (Firebase/MySQL)
- 📱 Mobile App Integration

---

## 👩‍💻 Author

**Tapila Mounika**

---

## 📄 License

This project is licensed under the MIT License.
