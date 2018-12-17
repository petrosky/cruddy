from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .models import Users, Task, TaskList
from django.utils import timezone
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TaskForm, AddUserForm, TaskDetailForm
from django.forms import formset_factory
from django.template import RequestContext
from django.shortcuts import render_to_response

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
            return HttpResponseRedirect(reverse('cruddy:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'cruddy/add_task.html', {'form': form})


def edit_task(request, task_id):

    context_instance = RequestContext(request)
    obj_list = Task.objects.all()

    if request.method == 'POST':
        e = Task.objects.get(pk=int(task_id))
        form = TaskForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/edit_task/')
    else:
        e = Task.objects.get(pk=int(task_id))
        form = TaskForm(instance=e)
    return render_to_response('cruddy/edit_task.html', {'form': form}, context_instance, )


def users(request):
    users = Users.objects.all()
    return render(request, 'cruddy/users.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddUserForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('cruddy:users'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddUserForm()
    return render(request, 'cruddy/add_user.html', {'form': form})


def tasks_by_user(request):

    users = Users.objects.all()

    return render(request, 'cruddy/tasks_by_user.html', {'users': users})


def tasks(request, user_id):

    user = get_object_or_404(Users, pk=user_id)
    task_list = Task.objects.filter(user_id=user_id)

    return render(request, 'cruddy/tasks.html', {'user': user, 'task_list': task_list})

