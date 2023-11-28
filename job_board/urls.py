from django.urls import path
from .views import index

# I denna fil har vi alla våra views som sedan importeras i urls.py filen i config-mappen.

urlpatterns = [
    path('', index),
]
