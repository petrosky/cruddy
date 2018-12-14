from django import forms
from .models import Task, TaskList, Users


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ()


class TaskDetailForm(forms.ModelForm):

    class Meta:
        model = TaskList
        exclude = ()


class AddUserForm(forms.ModelForm):

    class Meta:
        model = Users
        exclude = ()

