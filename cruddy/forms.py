from django.forms import ModelForm
from .models import Task, Users


class TaskForm(ModelForm):

    class Meta:
        model = Task
        exclude = ()




