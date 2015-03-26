from django.db import models

class Schedule(models.Model):
    def createTask(self, title, duration):
        task = Task(schedule=self, title=title, duration=duration)
        task.save()
        return task

class Task(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tasks',
        help_text = 'The schedule to which the task belongs.',
    )

    title = models.CharField(
        max_length=255,
        help_text = 'The title of the task.',
    )

    duration = models.PositiveIntegerField(
        default=600,
        help_text = 'The (estimated) duration of the task, in seconds.',
    )

