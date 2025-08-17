from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import numpy as np
import os

# Load the face data and labels
try:
    with open('data/faces_data.pkl', 'rb') as f:
        raw_faces = pickle.load(f)
    with open('data/names.pkl', 'rb') as f:
        labels = pickle.load(f)
except FileNotFoundError:
    print("Error: Make sure 'faces_data.pkl' and 'names.pkl' exist in the 'data/' folder.")
    exit()

# Sanitize and flatten face images
faces = []
valid_labels = []

for i, img in enumerate(raw_faces):
    if img is not None and img.shape == (50, 50, 3):
        faces.append(img.flatten())
        valid_labels.append(labels[i])
    else:
        print(f"Skipped face {i} due to invalid shape: {None if img is None else img.shape}")

faces = np.array(faces)
labels = np.array(valid_labels)

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(faces, labels, test_size=0.2, random_state=42)

# Train model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict
y_pred = knn.predict(X_test)

# Evaluation
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("\n🧮 Confusion Matrix:\n", cm)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=np.unique(labels), yticklabels=np.unique(labels))
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.tight_layout()
plt.show()
