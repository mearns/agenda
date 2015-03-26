from django.db import models
from ordered_model.models import OrderedModel


class Schedule(models.Model):
    def appendTask(self, task):
        """
        Append the given task to the end of the schedule.

        :param Task task: The `Task` to append.
        """
        if not isinstance(task, Task):
            raise TypeError('Not a task: %r' % (task,))

        self.tasks.add(task)
        task.bottom()

    def queryTasks(self):
        """
        Returns a query set of this schedule's tasks is the correct order.
        """
        return self.tasks.filter('index')


class Task(OrderedModel):
    order_with_respect_to = 'schedule'

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

    index = models.IntegerField(
        default=-1,
        editable=False,
        help_text = 'Defines the index of this task within the schedule. -1 means it has not yet been ordered.',
    )

