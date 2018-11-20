from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Users, Task, TaskList
from django.template import loader
from django.shortcuts import get_object_or_404, render


def index(request):
    tasks = Task.objects.order_by('due_date')
    template = loader.get_template('cruddy/index.html')
    context = {
        'tasks': tasks,
    }
    return HttpResponse(template.render(context, request))


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_list = TaskList.objects.filter(task_id=task_id)

    return render(request, 'cruddy/task_detail.html', {'task': task, 'task_list': task_list})


def add_task(request):

    return render(request, 'cruddy/add_task.html')