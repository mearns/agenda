# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'The title of the task.', max_length=255)),
                ('duration', models.PositiveIntegerField(default=600, help_text=b'The (estimated) duration of the task, in seconds.')),
                ('schedule', models.ForeignKey(related_name=b'tasks', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='agenda.Schedule', help_text=b'The schedule to which the task belongs.', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
