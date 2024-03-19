"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
