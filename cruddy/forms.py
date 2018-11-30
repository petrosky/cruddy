#from django import forms
from django.forms import ModelForm
from .models import Task, Users


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'due_date','user_id']