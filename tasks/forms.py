from django import forms


from tasks.models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'
