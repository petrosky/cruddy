from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Task
from django.template import loader


def index(request):
    tasks = Task.objects.order_by('due_date')[:5]
    template = loader.get_template('cruddy/index.html')
    context = {
        'tasks': tasks,
    }
    return HttpResponse(template.render(context, request))