from django.urls import path
from .views import index, job_detail

# I denna fil har vi alla våra views som sedan importeras i urls.py filen i config-mappen.

urlpatterns = [
    path('', index, name='home'),
    path('job/<int:pk>/', job_detail, name='job-detail'),
]
