#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:
"""
Tests for the "create_schedule" user story.
"""

from django.test import TestCase
import random

from agenda import models

class CreateScheduleTestCase(TestCase):
    pass

class CreateSchedule(CreateScheduleTestCase):
    def test_create_empty_schedule(self):
        sched = models.Schedule()

class AppendTask(CreateScheduleTestCase):
    def setUp(self):
        self.rand = random.Random()
        self.rand.seed(20150326)
        self.tasks = []
        self.sched = models.Schedule()
        self.sched.save()
        self.sched_id = self.sched.id

    def createTask(self):
        taskNum = len(self.tasks)+1
        task = models.Task(title='Task #%d' % taskNum)
        task.save()
        self.tasks.append(task)
        return task

    def test_append_first_task(self):
        """
        Creates a task and appends it to an empty schedule, then verifies that it is
        accessible from the schedule.
        """
        task = self.createTask()
        self.assertIs(task.schedule, None)

        ##Append it
        self.sched.appendTask(task)

        ## Make sure the task has the correct schedule associated.
        self.assertEqual(task.schedule.id, self.sched.id)

        ## Make sure the schedule has the task.
        tasks_qs = self.sched.tasks
        self.assertEqual(tasks_qs.count(), 1)
        self.assertEqual(tasks_qs.all()[0].id, task.id)

    def test_append_second_task(self):
        """
        Creates two taks and appends them to an empty schedule, then verifies that they are
        accessible in order from the schedule.
        """
        self.test_append_first_task()

        task = self.createTask()
        self.assertIs(task.schedule, None)

        ##Append it
        self.sched.appendTask(task)

        ## Make sure the task has the correct schedule associated.
        self.assertEqual(task.schedule.id, self.sched.id)

        ## Make sure the schedule has the task.
        tasks_qs = self.sched.tasks
        self.assertEqual(tasks_qs.count(), 2)
        self.assertEqual(tasks_qs.all()[1].id, task.id)

    def test_append_many_tasks(self):
        tasks = [self.createTask() for i in xrange(50)]
        self.rand.shuffle(tasks)
        for i in xrange(len(tasks)):
            task = tasks[i]
            self.assertIs(task.schedule, None)

            ##Append it
            self.sched.appendTask(task)

            ## Make sure the task has the correct schedule associated.
            self.assertEqual(task.schedule.id, self.sched.id)

            ## Make sure the schedule has the task.
            tasks_qs = self.sched.tasks
            self.assertEqual(tasks_qs.count(), i+1)
            self.assertEqual(tasks_qs.all()[i].id, task.id)


