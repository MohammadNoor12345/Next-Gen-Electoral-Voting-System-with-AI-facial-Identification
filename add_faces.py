import cv2
import os
import pickle

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces_data = []
labels = []

name = input("Enter Voter ID: ")

if not os.path.exists('data'):
    os.makedirs('data')

print(f"Collecting images for Voter ID {name}...")

count = 0
while True:
    ret, frame = video.read()
    if not ret:
        continue
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50))
        faces_data.append(resized_img)
        labels.append(name)
        count += 1
        cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if count >= 100:
        break

video.release()
cv2.destroyAllWindows()

# Save the data
with open("data/faces_data.pkl", "wb") as f:
    pickle.dump(faces_data, f)

with open("data/names.pkl", "wb") as f:
    pickle.dump(labels, f)

print("Face data collected successfully.")
