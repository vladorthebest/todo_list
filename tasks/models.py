from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Tasks Model
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255) #name tasks 
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True) #date create tasks

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['status']
    