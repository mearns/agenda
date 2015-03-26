from django.db import models

class Schedule(models.Model):
    def createTask(self, title, duration):
        task = Task(schedule=self, title=title, duration=duration)
        task.save()
        return task

class Task(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, related_name='tasks')
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()

