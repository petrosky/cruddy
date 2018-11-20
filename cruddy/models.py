from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_level = models.IntegerField()

    def __str__(self):
        return self.first_name


class Task(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=150)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.task_name


class TaskList(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_list = models.CharField(max_length=250)

    def __str__(self):
        return self.task_list

