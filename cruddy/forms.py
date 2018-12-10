from django.forms import ModelForm
from django import forms
from .models import Task, Users
from django.forms import inlineformset_factory


class TaskForm(ModelForm):

    class Meta:
        model = Task
        exclude = ()




