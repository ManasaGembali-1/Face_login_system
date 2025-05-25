
import cv2
import time
import os

FACES_DIR = "dataset"
if not os.path.exists(FACES_DIR):
    os.makedirs(FACES_DIR)

MAX_FACES = 5
PASSWORD = "admin123"

def log_registration(name):
    with open("registration_log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()}: Registered face '{name}'\n")

def alert_admin(name):
    print(f"ADMIN ALERT: New face registered: {name}")

def check_blink(eye_frames, blink_threshold=3):
    return eye_frames >= blink_threshold

def get_password():
    return input("Enter registration password: ")

def main():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    registered_faces = len(os.listdir(FACES_DIR))
    print(f"Registered faces count: {registered_faces}")

    registration_mode = False
    blink_frames = 0
    registering_name = None
    face_captured = False

    while True:   
        # cap is the webcam object created with cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            break
#         ret: a boolean indicating whether the frame was successfully captured (True or False)

# frame: the actual image/frame captured from the webcam

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_roi_gray = gray[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(face_roi_gray)
            if len(eyes) == 0:
                blink_frames += 1
            else:
                blink_frames = 0

            if registration_mode and not face_captured:
                cv2.putText(frame, "Please blink to confirm liveness", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                if check_blink(blink_frames):
                    face_img = frame[y:y+h, x:x+w]
                    filename = os.path.join(FACES_DIR, f"{registering_name}.jpg")
                    cv2.imwrite(filename, face_img)
                    print(f"Face registered for '{registering_name}'")
                    log_registration(registering_name)
                    alert_admin(registering_name)
                    registered_faces += 1
                    face_captured = True
                    registration_mode = False

        cv2.putText(frame, "Press 'r' to register, 'q' to quit", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        if registration_mode and not face_captured:
            cv2.putText(frame, f"Registering: {registering_name}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        cv2.imshow("Secure Face Registration", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r') and not registration_mode:
            if registered_faces >= MAX_FACES:
                print("Maximum number of faces registered.")
                continue
            pwd = get_password()
            if pwd == PASSWORD:
                registering_name = input("Enter your name: ").strip()
                if registering_name:
                    registration_mode = True
                    face_captured = False
                    blink_frames = 0
                else:
                    print("Name cannot be empty.")
            else:
                print("Incorrect password.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
