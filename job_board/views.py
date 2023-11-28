from django.shortcuts import render, get_object_or_404

# Måste importa models för att kunna hämta data
from .models import JobPost

# Create your views here.
def index(request):
    # En variabel som håller de job där is_active är true:
    active_postings = JobPost.objects.filter(is_active=True)
    # Dictionary som skickar data till the template. måste innehålla key-value pairs.
    context = {
        # Sätter job_postings som keyn och alla active postings som the value
        'job_postings': active_postings
        
    }
    return render(request, 'job_board/index.html', context)



def job_detail(request, pk):
    job_posting = get_object_or_404(JobPost, pk=pk, is_active=True)
    context = {
        'posting': job_posting
    }
    return render(request, 'job_board/detail.html', context)