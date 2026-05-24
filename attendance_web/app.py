from flask import Flask, render_template, request, redirect, url_for, session, send_file
import subprocess
import pandas as pd
import qrcode
import os

app = Flask(__name__)
app.secret_key = "secret123"

# 🔥 BASE PATH (IMPORTANT)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 👉 LOGIN PAGE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin123":
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Login ❌"

    return render_template('login.html')


# 👉 DASHBOARD
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


# 👉 START ATTENDANCE (🔥 FIXED)
@app.route('/start')
def start_attendance():
    if 'user' not in session:
        return redirect(url_for('login'))

    # Path to script
    script_path = os.path.join(BASE_DIR, "..", "attendance_system", "final_attendance.py")

    # 🔥 USE VENV PYTHON (IMPORTANT FIX)
    python_path = os.path.join(BASE_DIR, "..", "attendance_system", "venv", "Scripts", "python.exe")

    print("Starting Attendance System...")
    print("Python Path:", python_path)
    print("Script Path:", script_path)

    subprocess.Popen([python_path, script_path], shell=True)

    return "Attendance System Started!"


# 👉 VIEW ATTENDANCE (🔥 FIXED PATH)
@app.route('/attendance')
def attendance():
    if 'user' not in session:
        return redirect(url_for('login'))

    file_path = os.path.join(BASE_DIR, "..", "attendance_system", "attendance.csv")

    try:
        df = pd.read_csv(file_path)
        data = df.to_dict(orient="records")
    except:
        data = []

    return render_template("attendance.html", data=data)


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    try:
        name = request.form['name']
        student_id = request.form['student_id']

        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")

        data = f"{name}_{student_id}_{today}"

        img = qrcode.make(data)

        folder = os.path.join(BASE_DIR, "qr_codes")
        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(folder, f"{student_id}.png")
        img.save(file_path)

        return send_file(file_path, as_attachment=True)

    except Exception as e:
        print("QR ERROR:", e)
        return f"Error generating QR: {e}"
@app.route('/register')
def register():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('register.html')
@app.route('/start_registration', methods=['POST'])
def start_registration():
    if 'user' not in session:
        return redirect(url_for('login'))

    name = request.form['name']
    student_id = request.form['student_id']

    import os
    import subprocess

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    script_path = os.path.join(BASE_DIR, "..", "attendance_system", "dataset_creator.py")
    python_path = os.path.join(BASE_DIR, "..", "attendance_system", "venv", "Scripts", "python.exe")

    # 🔥 pass ID to dataset script
    subprocess.Popen([python_path, script_path, student_id])
    return f"Registration started for {name} ({student_id})"

@app.route('/admin_panel')
def admin_panel():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('admin_panel.html')


# 👉 LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


# 👉 RUN APP
if __name__ == "__main__":
    app.run(debug=True)