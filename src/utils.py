import face_recognition
import numpy as np
import os
import datetime

def get_project_root():
    try:
        # Move two levels up from current file (assuming file inside src/)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    except NameError:
        # fallback for interactive sessions
        project_root = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))
    return project_root

def get_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) > 0:
        encoding = encodings[0].astype(np.float32)
        return encoding
    else:
        print(f"WARNING: No face found in {image_path}")
        return None

def get_attendance_file_path():
    project_root = get_project_root()
    attendance_folder = os.path.join(project_root, 'data', 'attendance')
    os.makedirs(attendance_folder, exist_ok=True)
    date_today = datetime.date.today().strftime('%Y-%m-%d')
    csv_filename = os.path.join(attendance_folder, f'attendance_{date_today}.csv')
    return csv_filename
