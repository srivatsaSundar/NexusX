from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class PostInfo(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True) 
    description=models.CharField(max_length=200, null=True)
    explain=models.CharField(max_length=500, null=True)
    image=models.ImageField(upload_to='media/images/', null=True)
    investment_file=models.FileField(upload_to='media/files/', null=True)
    time_stamp=models.DateTimeField(auto_now_add=True, null=True)
    average_investment=models.IntegerField(null=True)
    domain=models.CharField(max_length=200, null=True)