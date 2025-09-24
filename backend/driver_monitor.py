"""
driver_monitor.py
Main logic for Raspberry Pi-Powered Intelligent Driver Monitoring System.
Monitors driver using face detection and eye-tracking, triggers fatigue alerts.
"""
import cv2
import time
from alert import AlertSystem
from utils import detect_face, detect_eyes, is_fatigued

class DriverMonitor:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        self.alert = AlertSystem()
        self.face_detected = False
        self.fatigue_counter = 0
        self.last_alert_time = 0
        self.alert_interval = 30  # seconds

    def process_frame(self, frame):
        face = detect_face(frame)
        if face is not None:
            self.face_detected = True
            eyes = detect_eyes(frame, face)
            if not eyes:
                self.fatigue_counter += 1
            else:
                if is_fatigued(eyes):
                    self.fatigue_counter += 1
                else:
                    self.fatigue_counter = max(0, self.fatigue_counter - 1)
        else:
            self.face_detected = False
            self.fatigue_counter = 0

    def run(self):
        print("[INFO] Starting Driver Monitoring...")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("[ERROR] Camera read failed.")
                break
            self.process_frame(frame)
            if self.fatigue_counter > 20:
                now = time.time()
                if now - self.last_alert_time > self.alert_interval:
                    self.alert.send_alert("Fatigue detected! Please take a break.")
                    self.last_alert_time = now
            cv2.imshow('Driver Monitor', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    monitor = DriverMonitor()
    monitor.run()
