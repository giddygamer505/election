from django.db import models

# Create your models here.
class candidate(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)