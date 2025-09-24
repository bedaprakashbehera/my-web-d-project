"""
urls.py
URL configuration for monitor app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('status/', views.status, name='status'),
]
