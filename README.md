# Face_login_system

# Secure Face Recognition Registration and Login System

This project implements a secure face recognition system that allows users to register their faces with liveness detection (blink check) and then log in via face recognition using a webcam.

---

## Features

- **Face Registration with Liveness Detection:**  
  Users can register their faces by providing a password and performing a blink to confirm liveness, preventing spoofing using photos or videos.

- **Face Encoding Generation:**  
  Encodes registered faces into 128-dimensional vectors and stores them for later recognition.

- **Face Login:**  
  Uses the webcam to detect faces and match them against registered face encodings to authenticate users.

- **Admin Alert and Logging:**  
  Logs each registration event with timestamps and prints an alert on new registrations.

---

## Repository Structure

- `register_faces.py` - Script for registering new faces with liveness check and saving them in the dataset folder.
- `encode_faces.py` - Script to process all images in the dataset and generate a pickle file containing face encodings and names.
- `face_login.py` - Script to perform live face recognition login using the webcam.
- `dataset/` - Folder where registered face images are stored.
- `encodings.pickle` - Generated file storing face encodings and corresponding names.
- `registration_log.txt` - Log file storing registration timestamps and user names.

---

## Requirements

- Python 3.7 or higher
- OpenCV
- face_recognition
- numpy
- pickle (built-in)

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/secure-face-login.git
   cd secure-face-login
   ```

---

## TO RUN THE CODE :

- python secure_face_register.py(press r to start registration,enter pswd and username)
- python encode_faces.py
- python login.py
- press q at any time
