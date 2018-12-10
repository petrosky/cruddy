from django.urls import path

from . import views

app_name = 'cruddy'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('add_task', views.add_task, name='add_task'),
    path('tasks_by_user', views.tasks_by_user, name='tasks_by_user'),
    path('tasks/<int:user_id>/', views.tasks, name='tasks'),
]