from django.forms import ModelForm
from django import forms
from . models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','category','timeAlloted',]
        exclude=['overhead','timeStarted','timeCompleted']

