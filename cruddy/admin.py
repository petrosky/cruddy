from django.contrib import admin

from .models import Task, TaskList


class TaskInline(admin.TabularInline):
    model = TaskList
    extra = 3


admin.site.register(Task)
admin.site.register(TaskList)