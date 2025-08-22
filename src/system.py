import cv2
import face_recognition
import numpy as np
import datetime
import csv
import os
from utils import get_face_encoding, get_attendance_file_path

# Load known faces and names
known_face_encodings = []
known_face_names = []

for filename, name in [("data/student images/guido.jpg", "Guido van Rossum"),
                       ("data/student images/grace.jpg", "Grace Hopper"),
                       ("data/student images/linus.jpg", "Linus Torvalds")]:
    encoding = get_face_encoding(filename)
    if encoding is not None:
        known_face_encodings.append(encoding)
        known_face_names.append(name)

# Get CSV file path for attendance (relative to the project folder)
csv_filename = get_attendance_file_path()

recorded_names = set()
if os.path.exists(csv_filename):
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        for row in reader:
            if row:
                recorded_names.add(row[0])

# Initialize camera
cap = cv2.VideoCapture(0)

# Attendance window duration (2 hours for testing)
attendance_close_time = datetime.datetime.now() + datetime.timedelta(minutes=120)

def mark_attendance(name):
    if name not in recorded_names:
        with open(csv_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            now = datetime.datetime.now().strftime('%H:%M:%S')
            writer.writerow([name, now])
        recorded_names.add(name)

# Create CSV file if it doesn't exist
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Time of Entry'])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Use the face_recognition library’s functions directly
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances) if len(face_distances) > 0 else None
        if best_match_index is not None and matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        if name != "Unknown":
            mark_attendance(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Face Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or datetime.datetime.now() > attendance_close_time:
        break

cap.release()
cv2.destroyAllWindows()

all_students = set(known_face_names)
present_students = recorded_names
absent_students = all_students - present_students

if absent_students:
    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for student in absent_students:
            writer.writerow([student, 'Absent'])

print('Attendance marked and saved to', csv_filename)
