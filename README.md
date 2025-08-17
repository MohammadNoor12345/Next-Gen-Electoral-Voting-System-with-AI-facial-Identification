
# Next-Gen Electoral Voting System with AI Facial Identification

## 📌 Overview

The **Next-Gen Electoral Voting System** is an AI-powered solution designed to modernize the voting process by replacing traditional manual verification with **facial recognition technology**. It leverages **Haar Cascade classifiers** for face detection and the **K-Nearest Neighbor (KNN)** algorithm for recognition, ensuring secure, fast, and contactless voter authentication.

This system prevents duplicate votes, reduces fraud, supports remote access, and lays the foundation for a **blockchain-based national voting system** in the future.

---

## ✨ Key Features

* 🔐 **AI Facial Recognition (Haar Cascade + KNN)** for accurate voter authentication.
* ⚡ **Fast & Secure**: Eliminates long queues and slow manual verification.
* 📱 **Remote Access**: Voters can cast votes using their mobile or laptop cameras.
* 🛡️ **Fraud Prevention**: Prevents duplicate or unauthorized voting.
* 🌍 **Scalable**: Can be integrated with blockchain for national-level deployment.

---

## 🛠️ Technologies Used

* **Python (CV2, Numpy, Pickle, Scikit-learn)**
* **OpenCV (Haar Cascade Classifier)**
* **K-Nearest Neighbor (KNN) Algorithm**
* **CSV for vote storage**
* **Speech Feedback (pywin32)**

---

## 📂 Project Structure

```
├── add_faces.py       # Collects and stores facial data of voters  
├── give_vote.py       # Face recognition & voting system  
├── Votes.csv          # Stores casted votes (Name, Vote, Date, Time)  
├── data/              # Stores facial data & labels (pickle files)  
```

---

## 🚀 Future Enhancements

* 🔗 Blockchain integration for tamper-proof voting.
* 📊 Real-time results dashboard.
* 🔄 Multi-factor authentication (Face + OTP).
* 🌐 Nationwide deployment for digital elections.

---

## 📖 How It Works

1. **Face Registration**: Collects 100 face samples of each voter.
2. **Face Recognition**: Identifies voter using KNN model.
3. **Vote Casting**: Voter casts vote (A/B/C).
4. **Vote Recording**: Vote securely stored in `Votes.csv`.
5. **Fraud Prevention**: Duplicate voting is automatically blocked.





