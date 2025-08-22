# facial-recognition-attendance-system
Facial recognition-based attendance system using Python and OpenCV. Automatically records student attendance in daily CSV files :D

## 🚀 Features:
- Detects whether a human face is present in the camera frame.
- Compares the detected face with the **known student faces database**.
- Marks attendance in a **CSV file** with:
  - Student name
  - Time of entry
- Automatically creates a **new CSV file for each day**.
- After a specific cutoff time, all students not marked as present will be labeled as **absent**.

## 🗂 Project Structure:
```
facial-recognition-attendance/
│
├── src/
│ ├── system.py # Main script
│ ├── utils.py # Helper functions
│ └──  known_faces.py # Known encodings & names
│
├── data/
│ ├── student_images/ # Student face images
│ └── attendance/ # Attendance CSV logs
│
├── requirements.txt # Dependencies
├── README.md # Documentation
└── .gitignore
```
## ▶️ Usage:

1. Add student images inside data/student_images/
   - File name format: name.jpg (e.g., guido.jpg)

2. Encode faces by updating src/known_faces.py:
```known_face_encodings = [...]```
```known_face_names = [...]```
3. Run the system:
```python src/system.py```
4. Attendance logs will be saved in `data/attendance/`

## 📦 Requirements:
- Python 3.8+
- face_recognition
- OpenCV (cv2)
- Numpy
- Pandas

## 🤝 Contributing:
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 💡 Note for Front-End Developers:
This project can also serve as a **practice backend system** for front-end developers.  
You can build a custom **UI dashboard** to visualize attendance data, integrate it with the generated CSV files, or even extend it into a full **web application**.

