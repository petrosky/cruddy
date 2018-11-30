#from django import forms
from django.forms import ModelForm
from .models import Task, Users


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'due_date']