#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:
"""
Tests the "Minimal agenda construction" user stories.
"""

from django.test import TestCase

from agenda import models

class MinimalTests(TestCase):
    pass

class MinimalProgrammaticTests(MinimalTests):
    def setUp(self):
        self.schedule = models.Schedule()
        self.task1 = self.schedule.createTask('first task', 5*60)
        self.task2 = self.schedule.createTask('second task', 10*60)
        self.task3 = self.schedule.createTask('third task', 1*60)
        self.task4 = self.schedule.createTask('fourth task', 30*60)

    def test_criteria_tasks(self):
        self.assertIs(self.schedule.getTask(0), self.task1)
        self.assertIs(self.schedule.getTask(1), self.task2)
        self.assertIs(self.schedule.getTask(2), self.task3)
        self.assertIs(self.schedule.getTask(3), self.task4)

