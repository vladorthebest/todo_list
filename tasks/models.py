from turtle import title
from django.db import models

# Tasks Model
class Task(models.Model):
    title = models.CharField(max_length=255) #name tasks 
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True) #date create tasks
    
 
    def __str__(self):
        return self.title
    