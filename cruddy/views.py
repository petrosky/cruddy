from django.http import HttpResponse
from .models import Users, Task, TaskList
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import TaskForm, UserForm


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
            form.save()
            # redirect to a new URL:
            return render(request, 'cruddy/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()
    return render(request, 'cruddy/add_task.html', {'form': form})


def users(request):
    users = Users.objects.all()
    return render(request, 'cruddy/users.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return render(request, 'users/add_user')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'cruddy/add_user.html', {'form': form})


def tasks_by_user(request):

    users = Users.objects.all()

    return render(request, 'cruddy/tasks_by_user.html', {'users': users})


def tasks(request, user_id):

    user = get_object_or_404(Users, pk=user_id)
    task_list = Task.objects.filter(user_id=user_id)

    return render(request, 'cruddy/tasks.html', {'user': user, 'task_list': task_list})

