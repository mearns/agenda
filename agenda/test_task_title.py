#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:
"""
Tests for the "task_title" user story.
"""

from django.test import TestCase

from agenda import models

class TaskTitleTestCase(TestCase):
    pass

class Setter(TaskTitleTestCase):
    def test_simple_title(self):
        task = models.Task(title='This is my task.')

    def test_long_title(self):
        title = 'abcdefghijklmnopqrstuvwxyz'
        title = title*10
        title = title[:255]
        self.assertEqual(len(title), 255)
        task = models.Task(title=title)

class Getter(TaskTitleTestCase):
    def test_simple_title(self):
        title = 'This is my task.'
        task = models.Task(title=title)
        self.assertEqual(task.title, title)

    def test_long_title(self):
        title = 'abcdefghijklmnopqrstuvwxyz'
        title = title*10
        title = title[:255]
        self.assertEqual(len(title), 255)
        task = models.Task(title=title)
        self.assertEqual(task.title, title)

class SaveRestore(TaskTitleTestCase):
    def test_simple_title(self):
        title = 'This is my task.'
        task = models.Task(title=title)

        task.save()
        pk = task.pk
        qtask = models.Task.objects.get(pk=pk)
        self.assertEqual(qtask.title, title)

    def test_long_title(self):
        title = 'abcdefghijklmnopqrstuvwxyz'
        title = title*10
        title = title[:255]
        self.assertEqual(len(title), 255)
        task = models.Task(title=title)
        
        task.save()
        pk = task.pk
        qtask = models.Task.objects.get(pk=pk)
        self.assertEqual(qtask.title, title)

