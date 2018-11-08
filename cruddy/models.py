from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_level = models.IntegerField()


class Tasks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=150)
    due_date = models.DateTimeField()


class TaskList(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    task_list = models.CharField(max_length=250)

