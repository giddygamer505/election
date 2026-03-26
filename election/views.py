from django.shortcuts import render
from .models import Candidate
from django.db.models import F

# Create your views here.
def home(request):
    candidates = Candidate.objects.all().order_by('name')
    return render(request, 'home.html', {'candidates': candidates})

def vote(request):
    pass