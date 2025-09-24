"""
utils.py
Utility functions for face and eye detection, and fatigue analysis.
"""
import cv2
import numpy as np

# Load Haar cascades (use OpenCV's default XMLs)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return None
    # Return the first face found
    return faces[0]

def detect_eyes(frame, face):
    x, y, w, h = face
    roi_gray = cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(roi_gray)
    return eyes

def is_fatigued(eyes):
    # Simple fatigue logic: if eyes are closed (no eyes detected)
    if len(eyes) == 0:
        return True
    # More advanced: check eye aspect ratio (EAR) for blink/fatigue
    # Placeholder for actual EAR calculation
    # For demo, randomly simulate fatigue
    import random
    return random.random() < 0.05

class AlertSystem:
    def send_alert(self, message):
        print(f"[ALERT] {message}")
        # Here you could add GPIO buzzer/light code for Raspberry Pi
        # Example: GPIO.output(buzzer_pin, GPIO.HIGH)
        # time.sleep(1)
        # GPIO.output(buzzer_pin, GPIO.LOW)

# For testing utils independently
if __name__ == "__main__":
    import sys
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        face = detect_face(frame)
        if face is not None:
            eyes = detect_eyes(frame, face)
            print(f"Eyes detected: {len(eyes)}")
        cv2.imshow('Test Utils', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
