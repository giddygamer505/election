from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class VoteRecord(models.Model):
    # เก็บเลขไอดี (ห้ามซ้ำ)
    voter_id = models.CharField(max_length=20, unique=True) 
    timestamp = models.DateTimeField(auto_now_add=True)