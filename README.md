# AI-Based-Attendance-System
AI-Based Attendance System Using Facial Recognition A smart attendance solution that uses facial recognition to automatically detect and mark attendance from CCTV or webcam images. Built with Python, OpenCV, and deep learning, this system improves efficiency and eliminates manual errors in attendance tracking.

AI-Based Attendance System Using Facial Recognition

## 📌 Overview

This project is an AI-powered attendance system that captures real-time images from CCTV or webcam footage, detects and recognizes faces using facial recognition algorithms, and automatically marks attendance in a secure and organized format.

## 🎯 Objective

To automate the attendance process using facial recognition, reducing manual errors and ensuring efficiency, especially in educational or organizational settings.

## 🔧 Features

🔍 Face detection and recognition from static or live video feeds
🧠 Uses pre-trained deep learning models for accurate recognition
📸 Attendance logging with timestamps
📁 Excel/CSV export of attendance records
🖥️ User-friendly interface (CLI or basic GUI)
🔐 Secured database of registered faces

## 🛠️ Tech Stack

Language: Python
Libraries: OpenCV, face_recognition, NumPy, Pandas
Database: CSV / SQLite (optional)
Camera Feed: CCTV / Webcam (via OpenCV)

## 🖼️ Sample Workflow

Register face(s) by capturing and storing labeled images
Load camera feed (live or screenshot)
Detect faces in frame
Match with known faces
Mark attendance with date and time
Export data to CSV/Excel

## 📂 Directory Structure
AI-Attendance-System/
├── dataset/              # Registered face images
├── attendance.csv        # Output file
├── register.py           # Face registration script
├── recognize.py          # Main script for face recognition & attendance
├── requirements.txt      # Dependencies
└── README.md             # This file

## 🧪 How to Run

Clone the repo
Install dependencies
pip install -r requirements.txt
Register users (faces) using register.py
Run recognize.py to start attendance from webcam/CCTV screenshot
View attendance.csv for records
