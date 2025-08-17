import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch
from sklearn.neighbors import KNeighborsClassifier

def speak(str1):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str1)

def check_if_exists(value):
    if not os.path.exists('Votes.csv'):
        return False
    with open('Votes.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0] == value:
                return True
    return False

# Load Data
with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)
with open('data/faces_data.pkl', 'rb') as f:
    raw_faces = pickle.load(f)

FACES = [img.flatten() for img in raw_faces if img is not None]
LABELS = [LABELS[i] for i in range(len(raw_faces)) if raw_faces[i] is not None]
FACES = np.array(FACES)
LABELS = np.array(LABELS)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

COL_NAMES = ["NAME", "VOTE", "DATE", "TIME"]

while True:
    ret, frame = video.read()
    if not ret:
        continue
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        voter_id = output[0]

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(frame, str(voter_id), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        if check_if_exists(voter_id):
            speak("You have already voted.")
            cv2.putText(frame, "Already Voted", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            continue

        speak("Please cast your vote.")
        vote = input(f"{voter_id}, Enter your vote (A/B/C): ").upper()
        while vote not in ['A', 'B', 'C']:
            vote = input("Invalid input. Please enter A/B/C: ").upper()

        # Save vote
        with open("Votes.csv", "a", newline='') as f:
            writer = csv.writer(f)
            if os.stat("Votes.csv").st_size == 0:
                writer.writerow(COL_NAMES)
            writer.writerow([voter_id, vote, date, timestamp])
        speak("Vote recorded successfully.")

    cv2.imshow("Voting System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()