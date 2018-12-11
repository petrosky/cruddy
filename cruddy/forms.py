from django.forms import ModelForm
from .models import Task, TaskList


class TaskForm(ModelForm):

    class Meta:
        model = Task
        exclude = ()


class TaskDetailForm(ModelForm):

    class Meta:
        model = TaskList
        exclude = ()



