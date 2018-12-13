from django.forms import ModelForm
from .models import Task, TaskList, Users


class TaskForm(ModelForm):

    class Meta:
        model = Task
        exclude = ()


class TaskDetailForm(ModelForm):

    class Meta:
        model = TaskList
        exclude = ()


class UserForm(ModelForm):

    class Meta:
        model = Users
        exclude = ()

