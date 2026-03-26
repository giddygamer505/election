from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate, VoteRecord
from django.db.models import F

# 1. หน้า Login (ใส่แค่ไอดี)
def login_view(request):
    if request.method == 'POST':
        voter_id = request.POST.get('voter_id').strip()
        if voter_id:
            request.session['voter_id'] = voter_id 
            return redirect('election:home')
    return render(request, 'login.html')

def home(request):
    voter_id = request.session.get('voter_id')
    if not voter_id:
        return redirect('election:login') 
    
    candidates = Candidate.objects.all().order_by('-votes')
    return render(request, 'home.html', {
        'candidates': candidates,
        'voter_id': voter_id
    })

def vote(request, candidate_id):
    voter_id = request.session.get('voter_id')
    
    if VoteRecord.objects.filter(voter_id=voter_id).exists():
        return render(request, 'home.html', {
            'candidates': Candidate.objects.all(),
            'error': 'คุณได้ใช้สิทธิ์โหวตไปแล้ว!'
        })

    if request.method == 'POST':
        # บันทึกว่าโหวตแล้ว และบวกคะแนน
        VoteRecord.objects.create(voter_id=voter_id)
        Candidate.objects.filter(id=candidate_id).update(votes=F('votes') + 1)
        
        del request.session['voter_id']
        return render(request, 'home.html') 

    return redirect('election:home')