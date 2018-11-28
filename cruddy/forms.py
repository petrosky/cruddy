from django import forms

from .models import Task


class TaskForm(forms.Form):
    task_name = forms.CharField(label = 'Task Name', max_length= 100)
    due_date = forms.DateField()