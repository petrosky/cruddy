from django.http import HttpResponse,HttpResponseRedirect
from .models import Users, Task, TaskList
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, render
from .forms import TaskForm


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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'cruddy/add_task.html', {'form': form})

def tasks_by_user(request):
    users = Users.objects.all()


    return render(request, 'cruddy/tasks_by_user.html', {'users': users})


