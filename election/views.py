from django.shortcuts import render
from .models import Candidate
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def home(request):
    candidates = Candidate.objects.all().order_by('name')
    return render(request, 'home.html', {'candidates': candidates})

def vote(request,candidate_id):
    if request.method == 'POST':
        candidate = get_object_or_404(Candidate, pk=candidate_id)
        Candidate.objects.filter(pk=candidate_id).update(votes=F('votes') + 1)
        return redirect('election:home') 
        
    return redirect('election:home')

def login(request):
    if request.method == 'POST':
        voter_id = request.POST.get('voter_id').strip()
        if voter_id:
            request.session['voter_id'] = voter_id
            return redirect('election:home')
    return render(request, 'login.html')