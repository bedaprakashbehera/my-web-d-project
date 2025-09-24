"""
models.py
No models needed for basic monitoring, but you can add logs or user models here.
"""
from django.db import models

# Example model for logging driver events
class DriverEvent(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return f"{self.timestamp}: {self.event_type}"
