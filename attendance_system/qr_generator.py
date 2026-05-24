import qrcode
import os
from datetime import datetime

# Create folder
if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")

# Input details
student_name = input("Enter Student Name: ").strip().replace(" ", "")
student_id = input("Enter Student ID: ").strip()

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")

# QR Data
qr_data = f"{student_name}_{student_id}_{today}"

# Generate QR
qr = qrcode.make(qr_data)

# Save QR
file_path = f"qr_codes/{student_id}.png"
qr.save(file_path)

print(f"QR generated: {qr_data}")