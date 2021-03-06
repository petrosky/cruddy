from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'cruddy'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('add_task', views.add_task, name='add_task'),
    path('tasks_by_user', views.tasks_by_user, name='tasks_by_user'),
    path('tasks/<int:user_id>/', views.tasks, name='tasks'),
    path('tasks/edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('users/', views.users, name='users'),
    path('users/add_user', views.add_user, name="add_user"),
    path('add_user', views.add_user, name="add_user"),
    path('edit_task/', views.edit_task, name='edit_task'),
]