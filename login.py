
import face_recognition
import cv2
import pickle
import time

def load_encodings():
    with open("encodings.pickle", "rb") as f:
        return pickle.load(f)

data = load_encodings()

video = cv2.VideoCapture(0)
print("🔐 Look at the camera to login...")

attempts = 0
max_attempts = 10

while True:
    ret, frame = video.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    name = "Unknown"
    if encodings:
        for encoding in encodings:
            distances = face_recognition.face_distance(data["encodings"], encoding)
            if len(distances) == 0:
                continue
            min_distance = min(distances)
            tolerance = 0.45
            if min_distance < tolerance:
                best_match_index = distances.tolist().index(min_distance)
                name = data["names"][best_match_index]
                print(f"✅ Login successful! Welcome, {name}.")
                cv2.putText(frame, f"Welcome {name}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Face Login", frame)
                cv2.waitKey(2000)
                video.release()
                cv2.destroyAllWindows()
                exit()

    cv2.putText(frame, name, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Face Login", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        print("❌ Login cancelled.")
        break

    attempts += 1
    if attempts >= max_attempts:
        print("❌ Login failed after max attempts.")
        break

video.release()
cv2.destroyAllWindows()
