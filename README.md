<img width="1920" height="1080" alt="Screenshot 2026-05-24 211322" src="https://github.com/user-attachments/assets/c7d4bbe0-0807-49f8-993b-193d5063c90a" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 211313" src="https://github.com/user-attachments/assets/423adbd9-ff85-42fb-a94e-1fc5ab92e0ec" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 211250" src="https://github.com/user-attachments/assets/a778403d-69ed-436c-8761-0174deb7507c" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 210914" src="https://github.com/user-attachments/assets/3d9b72f4-d45b-4852-b4e3-5aec4a241aaa" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 210905" src="https://github.com/user-attachments/assets/d44528c9-3623-474f-99a5-2c28c3bfdc7d" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 210847" src="https://github.com/user-attachments/assets/843622db-537a-4008-a21e-d2483ab0bf4c" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 210830" src="https://github.com/user-attachments/assets/7c259908-a620-466d-8ca6-9b4f1698d09e" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 210817" src="https://github.com/user-attachments/assets/88b13f7e-e941-44e4-bcb1-687e7266c564" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 210646" src="https://github.com/user-attachments/assets/86034c26-989a-4793-99d1-b497659e23c8" />
<img width="1920" height="1080" alt="Screenshot 2026-05-24 204153" src="https://github.com/user-attachments/assets/91881ab8-7823-4b6d-a4a9-dc0a7cc10be0" />
<img width="708" height="593" alt="Screenshot 2026-05-18 225758" src="https://github.com/user-attachments/assets/601e9857-ceab-42e4-9cf6-3aa7c09a01c0" />
<img width="1920" height="1080" alt="Screenshot 2026-05-12 122654" src="https://github.com/user-attachments/assets/a1db055e-5267-4d95-9115-1aad68f8acb6" />
<img width="1920" height="1080" alt="Screenshot 2026-05-11 133900" src="https://github.com/user-attachments/assets/69db2802-bb87-4ef9-9686-6cfab659967f" />
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
