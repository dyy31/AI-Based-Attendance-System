import face_recognition
import os
import pickle
import pandas as pd
from datetime import datetime


# Load Student Metadata

student_metadata = pd.read_csv("students_database.csv")
student_metadata.set_index("EnrollmentNumber", inplace=True)

# Define the intended class
TARGET_SECTION = "4X"
TARGET_COURSE = "B.Tech CSE"
TARGET_YEAR = 4


# STEP 1: Register Students

dataset_path = "Dataset"

known_encodings = []
student_ids = []

for student_folder in os.listdir(dataset_path):
    student_path = os.path.join(dataset_path, student_folder)
    if not os.path.isdir(student_path):
        continue

    for image_file in os.listdir(student_path):
        image_path = os.path.join(student_path, image_file)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            student_ids.append(student_folder)

# Save encodings
with open("encodings.pkl", "wb") as f:
    pickle.dump((known_encodings, student_ids), f)

print("[INFO] Student face encodings saved.")

# STEP 2: Process CCTV Screenshot

with open("encodings.pkl", "rb") as f:
    known_encodings, student_ids = pickle.load(f)

cctv_image_path = "3-idiots.jpg.webp"
cctv_image = face_recognition.load_image_file(cctv_image_path)

face_locations = face_recognition.face_locations(cctv_image)
face_encodings = face_recognition.face_encodings(cctv_image, face_locations)

present_students = set()

for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_encodings, face_encoding)
    face_distances = face_recognition.face_distance(known_encodings, face_encoding)
    best_match_index = face_distances.argmin()
    if matches[best_match_index]:
        student_id = student_ids[best_match_index]
        present_students.add(student_id)

print(f"[INFO] Students present in image: {present_students}")


# STEP 3: Mark Attendance in CSV

attendance_filename = f"attendance_{datetime.now().date()}.csv"
current_time = datetime.now().strftime("%H:%M:%S")

attendance_data = []

for student_id in set(student_ids):
    if student_id in present_students:
        # Check if student belongs to this class
        if student_id in student_metadata.index:
            student_info = student_metadata.loc[student_id]
            if (
                student_info["Section"] == TARGET_SECTION and
                student_info["Course"] == TARGET_COURSE and
                int(student_info["Year"]) == TARGET_YEAR
            ):
                status = "Present"
            else:
                status = "Wrong Class"
        else:
            status = "Unknown"
        time_str = current_time
    else:
        status = "Absent"
        time_str = "-"

    attendance_data.append({
        "StudentID": student_id,
        "Status": status,
        "Time": time_str
    })

attendance_df = pd.DataFrame(attendance_data)
attendance_df.to_csv(attendance_filename, index=False)
print(f"[INFO] Attendance saved to {attendance_filename}")
