import face_recognition

known_face_encodings = []
known_face_names = []

# Direct loading and encoding for Guido
guido_image = face_recognition.load_image_file("data/student images/guido.jpg")
guido_encoding = face_recognition.face_encodings(guido_image)
if len(guido_encoding) > 0:
    known_face_encodings.append(guido_encoding[0])
    known_face_names.append("Guido van Rossum")
else:
    print("WARNING: No face found in guido.jpg")

# Direct loading and encoding for Grace
grace_image = face_recognition.load_image_file("data/student images/grace.jpg")
grace_encoding = face_recognition.face_encodings(grace_image)
if len(grace_encoding) > 0:
    known_face_encodings.append(grace_encoding)
    known_face_names.append("Grace Hopper")
else:
    print("WARNING: No face found in grace.jpg")

# Direct loading and encoding for Linus
linus_image = face_recognition.load_image_file("data/student images/linus.jpg")
linus_encoding = face_recognition.face_encodings(linus_image)
if len(linus_encoding) > 0:
    known_face_encodings.append(linus_encoding)
    known_face_names.append("Linus Torvalds")
else:
    print("WARNING: No face found in linus.jpg")


# use of a helper function to add known faces properly
def add_face(filename, name):
    image = face_recognition.load_image_file(filename)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) > 0:
        known_face_encodings.append(encodings)
        known_face_names.append(name)
    else:
        print(f"WARNING: No face found in {filename}. Skipping.")


