
import face_recognition
import pickle
import os

dataset_dir = "dataset"
encodings = []
names = []

for filename in os.listdir(dataset_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Loops through all .jpg or .png files in the folder dataset_dir.
        # Each file is assumed to be a registered user's face image.
        img_path = os.path.join(dataset_dir, filename)
        image = face_recognition.load_image_file(img_path)
        # Builds the full path to the image.
        # Loads the image using the face_recognition library.
        face_locations = face_recognition.face_locations(image)
           #Detects face bounding boxes (coordinates) in the image.


        if face_locations:
            encoding = face_recognition.face_encodings(image, face_locations)[0]
            encodings.append(encoding)
            names.append(os.path.splitext(filename)[0])

           # Generates the 128-dimensional encoding (unique vector for the face).
            #Adds it to the list encodings.
            #Stores the name (taken from the filename without extension) to match with the encoding.
        else:
            print(f"⚠️ No face found in {filename}, skipping.")

data = {"encodings": encodings, "names": names}
with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)
   # Creates a dictionary containing all encodings and their corresponding names.

    #Saves it to a file encodings.pickle using Python’s pickle module.

   #This file is used later by your login system to compare with live camera input.



print("✅ Encodings saved successfully.")
