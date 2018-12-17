from django.contrib import admin

from .models import Users, Task, TaskList


class TaskInline(admin.TabularInline):
    model = TaskList
    extra = 3


admin.site.register(Users)
admin.site.register(Task)
admin.site.register(TaskList)
