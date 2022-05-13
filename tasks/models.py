from turtle import title
from django.db import models

# Tasks Model
class Task(models.Model):
    title = models.CharField(max_length=255) #name tasks 
    task = models.CharField(max_length=1000) #that you need to do
    date = models.DateField(auto_now=True) #date create tasks
    date_end = models.DateField() #until which date you need to do it
 
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']