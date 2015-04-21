# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('email', models.CharField(max_length=100)),
                ('signup_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTopic',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('last_update_time', models.DateTimeField()),
                ('topic_id', models.ForeignKey(to='signup_app.Topic')),
                ('user_id', models.ForeignKey(to='signup_app.User')),
            ],
        ),
    ]
