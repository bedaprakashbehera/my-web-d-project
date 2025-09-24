"""
views.py
Views for monitor app. Integrates driver_monitor logic and returns status to frontend.
"""
from django.shortcuts import render
from django.http import JsonResponse
import threading
import time

# Simulate driver status (replace with actual logic integration)
driver_status = {
    'face_detected': True,
    'fatigue_counter': 0,
    'last_alert': '',
}

def dashboard(request):
    return render(request, 'dashboard.html')

def status(request):
    # In real use, get live status from driver_monitor
    return JsonResponse(driver_status)

# Example: background thread to simulate status updates
def monitor_thread():
    import random
    while True:
        driver_status['face_detected'] = random.choice([True, False])
        driver_status['fatigue_counter'] = random.randint(0, 30)
        if driver_status['fatigue_counter'] > 20:
            driver_status['last_alert'] = 'Fatigue detected!'
        else:
            driver_status['last_alert'] = ''
        time.sleep(2)

threading.Thread(target=monitor_thread, daemon=True).start()
