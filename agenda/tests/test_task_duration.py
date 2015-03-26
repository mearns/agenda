#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:
"""
Tests for the "task_duration" user story.
"""

from django.test import TestCase

from agenda import models

class TaskDurationTestCase(TestCase):
    def setUp(self):
        self.task = models.Task(title='This is my task.')

class Setter(TaskDurationTestCase):
    def test_simple_duration(self):
        self.task.duration = 10*60

    def test_min_duration(self):
        self.task.duration = 1

    def test_max_duration(self):
        self.task.duration = 2147483647

class Getter(TaskDurationTestCase):
    def test_simple_duration(self):
        duration = 10*60
        self.task.duration = duration
        self.assertEqual(self.task.duration, duration)

    def test_min_duration(self):
        duration = 1
        self.task.duration = duration
        self.assertEqual(self.task.duration, duration)

    def test_max_duration(self):
        duration = 2147483647
        self.task.duration = duration
        self.assertEqual(self.task.duration, duration)

class SaveRestore(TaskDurationTestCase):
    def test_simple_duration(self):
        duration = 10*60
        self.task.duration = duration

        self.task.save()
        pk = self.task.pk
        qtask = models.Task.objects.get(pk = pk)
        self.assertEqual(qtask.duration, duration)

    def test_min_duration(self):
        duration = 1
        self.task.duration = duration

        self.task.save()
        pk = self.task.pk
        qtask = models.Task.objects.get(pk = pk)
        self.assertEqual(qtask.duration, duration)

    def test_max_duration(self):
        duration = 2147483647
        self.task.duration = duration

        self.task.save()
        pk = self.task.pk
        qtask = models.Task.objects.get(pk = pk)
        self.assertEqual(qtask.duration, duration)

