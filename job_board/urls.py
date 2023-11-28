from django.urls import path
from .views import index, job_detail

# I denna fil har vi alla våra views för själva appen. endast startsidan osv importeras till configens urls.py

urlpatterns = [
    path('', index, name='home'),
    path('job/<int:pk>/', job_detail, name='job-detail'),
]
