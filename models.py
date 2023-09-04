from django.db import models

# Create your models here.
# Project
class Project (models.Model):
    name = models.CharField(max_length = 60)
    time_created = models.DateTimeField(auto_now_add=True)
    estimated_completion = models.TextField()

    def __str__(self):
        return self.name
# Task
class Task (models.Model):
    task_name = models.CharField(max_length = 60)
    description = models.TextField(max_length = 200)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_for_completion = models.TextField(max_length = 20)
    completion_status = models.TextField(max_length = 10)

    def __str__(self):
        return self.task_name