from django.http import HttpResponse
from .models import Users, Task, TaskList
from django.template import loader
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .forms import TaskForm
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
            #task_name = request.POST.get('task_name')
            #due_date = request.POST.get('due_date')
            # redirect to a new URL:
            return render(request, 'cruddy/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()
    return render(request, 'cruddy/add_task.html', {'form': form})


def tasks_by_user(request):

    users = Users.objects.all()

    return render(request, 'cruddy/tasks_by_user.html', {'users': users})


def tasks(request, user_id):
    #return HttpResponse('<h1>Page was found</h1>')
    user = get_object_or_404(Users, pk=user_id)
    task_list = Task.objects.filter(user_id=user_id)

    return render(request, 'cruddy/tasks.html', {'user': user, 'task_list': task_list})

